import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import plotly.express as px

sales = pd.read_csv("sales.csv")
inv = pd.read_csv("inventory.csv")
prod = pd.read_csv("products.csv")

data = sales.merge(inv, on=["store_id","sku"], how="left")
data = data.merge(prod, on="sku", how="left")

data["demand_level"] = pd.qcut(data["quantity_sold"], q=3, labels=["low","medium","high"])
data["lead_level"] = pd.qcut(data["lead_time"], q=3, labels=["short","medium","long"])
data["cat_item"] = "cat_" + data["category"].astype(str)

records = data[["demand_level","lead_level","cat_item"]].astype(str).values.tolist()
te = TransactionEncoder()
te_ary = te.fit(records).transform(records)
df = pd.DataFrame(te_ary, columns=te.columns_)

freq = apriori(df, min_support=0.02, use_colnames=True)
rules = association_rules(freq, metric="confidence", min_threshold=0.5)
rules.to_csv("generated_rules.csv", index=False)

trend = data.groupby("week")["quantity_sold"].sum().reset_index()
fig1 = px.line(trend, x="week", y="quantity_sold")
fig1.write_image("demand_trend.png")

cat = data.groupby("category")["quantity_sold"].sum().reset_index()
fig2 = px.bar(cat, x="category", y="quantity_sold")
fig2.write_image("category_sales.png")
