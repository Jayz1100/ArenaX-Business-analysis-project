# NBA Market Intelligence

本项目整理自本次 **Week 1 NBA 英文市场研究报告**，可离线重生成四页 PDF、
独立扇形图和分析数据。附带的报告、数据和图表均可直接使用。

## Quick start

需要 Python 3.10 或以上版本。在项目目录打开终端：

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

也可以直接运行 `.venv\Scripts\python.exe main.py`，不必激活环境。
运行不需要 API key、网络或本机绝对路径；路径相对于项目所在目录。

## Project structure

```text
nba-market-intelligence/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   │   ├── evidence.json
│   │   ├── sources.json
│   │   └── research_brief.json
│   └── processed/
│       ├── metrics.json
│       ├── metrics.csv
│       ├── analysis.json
│       ├── market_distribution.csv
│       ├── research_plan.json
│       ├── source_inventory.json
│       └── validation.json
├── src/
│   ├── __init__.py
│   ├── planner.py
│   ├── search.py
│   ├── extractor.py
│   ├── analysis.py
│   ├── charts.py
│   └── report.py
├── outputs/
│   ├── charts/
│   │   ├── market_size_pie.svg
│   │   └── market_size_pie.pdf
│   └── nba_report.pdf
└── prompts/
    ├── planner.txt
    ├── extraction.txt
    └── analysis.txt
```

## 模块职责

| 模块 | 已实现功能 |
| --- | --- |
| planner.py | 从研究简要生成固定的 Week 1 工作计划 |
| search.py | 读取、按关键词查询本地来源目录 |
| extractor.py | 校验字段、单位、数值、来源和期间，整理事实记录 |
| analysis.py | 计算媒体合同年均值、赞助增速、球队倍数及示意分布 |
| charts.py | 导出带来源标注的 SVG、PDF 图表，并绘制报告内图表 |
| report.py | 使用已确认的英文版式、处理后数值和来源生成 PDF |

`search.py` 是本地来源检索，不调用网络搜索引擎；`extractor.py` 读取人工整理的
结构化证据，不抓取网页。`prompts/` 是未来接入模型时的模板，本次运行不会调用模型。
未配置自动联网采集、付费数据库访问或实时刷新。

## 数据来源和口径

`data/raw/` 指保留的人工整理事实与来源目录，并非下载的出版商原始数据库或网页快照。
数据来自原对话及生成 PDF 时核对的公开资料。`sources.json` 保留链接、用途和核对日期。
所有事实包含数值、单位、期间、证据状态与来源编号。

- 年收入：2024-25 NBA 30 队收入合计约 $12.5B。
- 球队估值：2025 Forbes 估值周期；估值与年收入不能混加。
- $77B 是媒体报道的合同金额；$7B 是 11 年合同的年均值。
- 赞助采用第三方估计；NBA 观众与观看次数属于不同口径。
- 饼图保留原报告的 56.0%、20.0%、14.4%、9.6%，明确标为跨赛季示意。
  门票为假设，其他为算术残差，**不能作为实际 NBA 收入结构**。

## 更新与复现

修改 `data/raw/evidence.json` 后运行 `python main.py`，处理数据、计算、图表和报告数值
会更新。报告保留固定的 Week 1 叙述、赛季文字与结论；若研究期间、来源或判断改变，
应同步审阅 `src/report.py` 和 `data/raw/sources.json`，尤其是图表口径。
数值更新不等于报告自动完成研究或自动确认结论。

`config.py` 控制路径和整理日期。执行时会覆盖本项目的处理数据、图表及 PDF。
结构校验包含四页页数、文本可提取性、必需指标、单位和来源关联。
本次交付另已渲染并人工检查 PDF 和图表；后续修改内容后应再次做视觉检查。

## 计算示例

```text
Media annual average = 77 / 11 = 7.0 (USD billion)
Sponsorship growth = (1.80 / 1.62 - 1) * 100 = 11.1%
Lakers / Hornets revenue = 551 / 328 = 1.68x
Illustrative residual = 12.5 - 7.0 - 2.5 - 1.8 = 1.2
```

图表使用 ReportLab 与标准库生成，无需系统字体、LaTeX、Poppler 或绘图库。
