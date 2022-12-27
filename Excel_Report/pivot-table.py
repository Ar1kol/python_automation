import pandas as pd

data_frame_all = pd.read_excel("supermarket_sales.xlsx")
df = data_frame_all[["Gender", "Product line", "Total"]]
pivot_table = df.pivot_table(index="Gender", columns="Product line", values="Total", aggfunc='sum').round(0)
pivot_table.to_excel("pivot_table.xlsx", "Report", startrow=4)