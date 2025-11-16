import pandas as pd
import plotly.express as px

sales = pd.read_csv("sales.csv")
inv = pd.read_csv("inventory.csv")
prod = pd.read_csv("products.csv")

data = sales.merge(inv, on=["store_id","sku"], how="left")
data = data.merge(prod, on="sku", how="left")

trend = data.groupby("week")["quantity_sold"].sum().reset_index()
px.line(trend, x="week", y="quantity_sold").show()

cat = data.groupby("category")["quantity_sold"].sum().reset_index()
px.bar(cat, x="category", y="quantity_sold").show()
