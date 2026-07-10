# bintel-02-mining

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: mining and exploring smart sales data.

## Project Description

This project focuses on reading raw business data into pandas DataFrames
for exploration and analysis.

We work with a realistic smart sales dataset containing
customers, products, and sales records.

We learn to:

- read raw CSV files into reusable pandas DataFrames
- inspect distributions of customers, products, and sales
- identify data quality issues that will need cleaning
- visualize price distributions and sales trends over time
- add reusable inspection and quality-check functions to the BI pipeline

## Working Files

You'll work with these areas:

- **data/raw** - raw smart sales CSV files (customers, products, sales)
- **docs/** - project narrative and documentation
- **src/bizintel/** - the app is an example; run only (no need to modify)
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions (pro-analytics-02)

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**,
you'll have your own GitHub project,
and running the example module will print out:

```shell
========================
Executed successfully!
========================
```

A new file `project.log` will appear in the root project folder.

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/nwmgraspr/bintel-02-mining

cd bintel-02-mining
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

```shell
uv self update
uv python pin 3.14
uv lock --upgrade
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
uvx pre-commit autoupdate

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
uvx pre-commit run --all-files

# run custom project module
uv run python -m bizintel.mining_ecommerce

# run common chores
uv run ruff format
uv run ruff check --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT need to understand everything; understanding builds naturally over time.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Example Output (Remove this Section after You Verify)

```shell
0 01:02:54 | INFO | BI | Quality check: customers
2026-07-10 01:02:54 | INFO | BI |   Total missing values: 0
2026-07-10 01:02:54 | INFO | BI |   Duplicate rows: 0
2026-07-10 01:02:54 | INFO | BI | Quality check: orders
2026-07-10 01:02:54 | INFO | BI |   Total missing values: 0
2026-07-10 01:02:54 | INFO | BI |   Duplicate rows: 0
2026-07-10 01:02:54 | INFO | BI | Quality check: web
2026-07-10 01:02:54 | INFO | BI |   Total missing values: 0
2026-07-10 01:02:54 | INFO | BI |   Duplicate rows: 0
2026-07-10 01:02:54 | INFO | BI | Numeric summary: orders
2026-07-10 01:02:54 | INFO | BI |
       OrderAmount
count        10.00
mean        115.75
std          90.41
min          25.00
25%          48.75
50%          94.99
75%         143.19
max         310.25
2026-07-10 01:02:54 | INFO | BI | Plotting order distribution
2026-07-10 01:02:56 | INFO | BI | Plotting revenue trend
2026-07-10 01:02:56 | INFO | BI | Creating chart: Monthly Revenue Trend
2026-07-10 01:02:57 | INFO | BI | Plotting engagement vs spending
2026-07-10 01:02:57 | INFO | BI | ========================
2026-07-10 01:02:57 | INFO | BI | SUMMARY
2026-07-10 01:02:57 | INFO | BI | ========================
2026-07-10 01:02:57 | INFO | BI | Customers: (8, 5)
2026-07-10 01:02:57 | INFO | BI | Orders:    (10, 5)
2026-07-10 01:02:57 | INFO | BI | Web:       (10, 5)
2026-07-10 01:03:03 | INFO | BI | Done.
```

## Findings and Visuals
Order Amount Distribution histogram is created to understand customer purchasing patterns. This helps identify typical order sizes and variation in spending behavior. Revenue Trend Analysis: Monthly revenue is calculated and displayed using a line chart. This reveals growth patterns, seasonal changes, and overall sales performance. Customer Engagement vs. Spending Analysis Website activity data is combined with order history. A scatter plot evaluates whether customers who spend more time on the website also generate higher revenue.

## Processes
The step is data inspection and quality analysis. Each dataset is loaded into a pandas DataFrame and examined for:
Dataset size (rows and columns) Column names and data types Missing values Duplicate records Basic data quality issues
This step ensures that the data is reliable before performing analysis. After validation, the project performs data preparation and transformation. Key transformations include: Converting order amounts into numeric values. Aggregating sales data by month to identify revenue patterns. Combining customer purchase data with web activity data to analyze relationships between engagement and spending.

# Custom Project Screenshots

![Engagement VS Spending](./docs/images/Figure_3.png)

![Monthly Revenue Trend](./docs/images/Figure_4.png)

![Order Amount Distribution](./docs/images/Figure_5.png)

## Project Documentation

Additional project instructions, terms, and notes:

[docs/index.md](docs/index.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
