import pandas as pd

curr = "USD"
excd_curr = "IDR"
val = 123.4

df = pd.read_csv(f"currency_dfs/{curr}_exchange.csv")

for i in range(len(df)):
    if excd_curr==df["currency"][i]:
        print(val*df["rate"][i])
