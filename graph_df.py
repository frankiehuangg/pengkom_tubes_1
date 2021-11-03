import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

def graph_df(from_curr, to_curr):
    curr_df = pd.read_csv(f"currency_dfs/{from_curr}/fx_daily_{from_curr}_{to_curr}.csv")

    x = [curr_df["date"][i] for i in range(len(curr_df))]
    y = [curr_df["rate"][i] for i in range(len(curr_df))]

    if y[-1]>y[0]:
        plt.plot(x,y,color='green')
        plt.fill_between(x,y,color='green',alpha=0.2)
    else:
        plt.plot(x,y,color='red')
        plt.fill_between(x,y,color='red',alpha=0.2)

    plt.axis((x[0],x[-1],min(y)-(min(y)/1000),max(y)+(min(y)/1000)))

    plt.xticks(x[::5],  rotation='vertical')
    plt.xlabel('Date')
    plt.title(f"{from_curr} to {to_curr} exchange")
    plt.subplots_adjust(left=0.15,
                        bottom=0.25,
                        right=0.97,
                        top=0.94,
                        wspace=0.2,
                        hspace=0.2)
    if not os.path.exists(f"graph_img/{from_curr}"):
        os.makedirs(f"graph_img/{from_curr}")
        
    plt.savefig(f"graph_img/{from_curr}/{to_curr}.png")

from_curr = input()
to_curr = input()

graph_df(from_curr, to_curr)
