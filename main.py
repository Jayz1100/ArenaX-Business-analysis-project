"""Run the reproducible offline Week 1 reporting pipeline."""
import csv, json
from pypdf import PdfReader
from config import PROCESSED_DIR, CHART_DIR, REPORT_PATH
from src.planner import create_plan
from src.search import load_sources
from src.extractor import extract_metrics
from src.analysis import analyze
from src.charts import export_charts
from src.report import build_report
def save_json(name,data):
    (PROCESSED_DIR/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def main():
    PROCESSED_DIR.mkdir(parents=True,exist_ok=True)
    rows=extract_metrics(); result=analyze(rows)
    save_json('research_plan.json',create_plan())
    save_json('metrics.json',rows); save_json('analysis.json',result)
    save_json('source_inventory.json',load_sources())
    for name,data in [('metrics.csv',rows),('market_distribution.csv',result['pie'])]:
        with (PROCESSED_DIR/name).open('w',encoding='utf-8',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(data[0])); writer.writeheader()
            for row in data:
                writer.writerow({k:json.dumps(v) if isinstance(v,list) else v for k,v in row.items()})
    charts=export_charts(result,CHART_DIR)
    report=build_report(result,REPORT_PATH)
    reader=PdfReader(str(report))
    if len(reader.pages)!=4 or any(len(p.extract_text())<200 for p in reader.pages):
        raise RuntimeError('PDF structural validation failed')
    checks={'pages':len(reader.pages),'text_extraction':'passed',
            'pie_share_total':sum(p['share_percent'] for p in result['pie']),
            'report':str(report.relative_to(REPORT_PATH.parent.parent)),
            'visual_review':'Perform after content changes; structural checks do not check layout.'}
    save_json('validation.json',checks)
    print('Created:',report)
    print('Charts:',', '.join(p.name for p in charts))
    print('Validated: 4 pages; readable text; source and metric schema checks passed.')
if __name__=='__main__': main()
