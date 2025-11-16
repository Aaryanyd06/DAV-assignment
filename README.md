# Retail Inventory Analytics – Rule Induction & Dashboard Project

This project implements a complete Data Analytics workflow for a fictional retail chain, RetailMax Stores, to optimize inventory using data preprocessing, feature engineering, rule induction (Apriori algorithm), and visualization (Plotly). The objective is to understand demand behavior and generate stocking rules to support better replenishment decisions.

<!-- ## Project Structure

Retail_Assignment/
  analysis.py
  dashboard_charts.py
  sales.csv
  inventory.csv
  products.csv
  generated_rules.csv
  demand_trend.png
  category_sales.png
  Inventory_Optimization_Case_Study.docx
  Rule_Induction_Report.docx -->

## How to Run the Project

1) Create and activate virtual environment:

        Windows:
        python -m venv venv
        venv\Scripts\activate

        macOS/Linux:
        python3 -m venv venv
        source venv/bin/activate

2) Install dependencies:
  pip install pandas numpy mlxtend plotly kaleido

3) Run full analysis:
  python analysis.py

        This generates:
        generated_rules.csv
        demand_trend.png
        category_sales.png

4) View dashboard charts:
  python dashboard_charts.py

## Outputs Included

- Association rules (Apriori)
- Weekly demand trend visualization
- Category-wise sales performance
- Word-document reports for academic submission

## Techniques Used

- Data Analytics Lifecycle
- Data Cleaning & Feature Engineering
- Categorical Discretization (qcut)
- Association Rule Mining (Apriori)
- Visualization with Plotly
- Kaleido image export

