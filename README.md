# Retail Inventory Analytics – Rule Induction & Dashboard Project

This project implements a complete Data Analytics workflow for a fictional retail chain, **RetailMax Stores**, to optimize inventory using data preprocessing, feature engineering, rule induction (Apriori algorithm), and visualization (Plotly). The goal is to understand demand behavior and generate stocking rules to assist store managers in making better replenishment decisions.

---

## 📁 Project Structure

Retail_Assignment/
│
├── analysis.py
├── dashboard_charts.py
│
├── sales.csv
├── inventory.csv
├── products.csv
│
├── generated_rules.csv
├── demand_trend.png
├── category_sales.png
│
├── Inventory_Optimization_Case_Study.docx
└── Rule_Induction_Report.docx

yaml
Copy code

---

## 🚀 How to Run the Project

### 1️⃣ Create and activate virtual environment

python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # macOS/Linux

shell
Copy code

### 2️⃣ Install dependencies

pip install pandas numpy mlxtend plotly kaleido

shell
Copy code

### 3️⃣ Run full analysis

python analysis.py

markdown
Copy code

Outputs generated:
- `generated_rules.csv`
- `demand_trend.png`
- `category_sales.png`

### 4️⃣ View dashboard charts

python dashboard_charts.py

yaml
Copy code

This opens interactive visualizations.

---

## 📊 Outputs Included

- Association rules (Apriori)
- Weekly demand trend visualization
- Category-wise sales performance
- Word-doc reports for academic submission

---

## 🔍 Techniques Used

- Data Analytics Lifecycle  
- Data Cleaning & Feature Engineering  
- Categorical Discretization (`qcut`)  
- Association Rule Mining (Apriori)  
- Visualization with Plotly  
- Kaleido-based image export  

---

## 👤 Author

Name: *Your Name*  
Course: Data Analytics & Visualization  

---

## 📜 License

Academic use only.