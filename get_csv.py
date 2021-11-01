import os
import csv
import requests
import bs4 as bs
import pandas as pd
from datetime import datetime,timedelta

def save_csv():
    curr_df = pd.read_csv("currency_dfs/physical_currency_list.csv")
    curr_list = [[curr_df["abbv"][i], curr_df["currency"][i]] for i in range(len(curr_df))]

    with open("currency_dfs/AED/fx_daily_AED_ARS.csv",'r') as f:
        last_line = f.readlines()[-1]

    last_date = last_line.split(',')[0]

    if last_date!=datetime.today():
        date_list = pd.date_range(datetime.strptime(last_date, '%Y-%m-%d')+timedelta(days=1), datetime.today())

        for day in date_list:
            for curr in curr_list:
                src = requests.get(f"https://www.x-rates.com/historical/?from={curr[0]}&amount=1&date={day.strftime('%Y-%m-%d')}")
                soup = bs.BeautifulSoup(src.text, "lxml")
                table = soup.find("table", {"class": "tablesorter ratesTable"})
                currs = []

                if not os.path.exists(f"currency_dfs/{curr[0]}"):
                    os.makedirs(f"currency_dfs/{curr[0]}")
        
                for row in table.findAll("tr")[1:]:
                    exchange = row.findAll("td")[1].find('a').contents[0]
                    currs.append([day.strftime('%Y-%m-%d'),exchange])

                for row in currs:
                    if not os.path.exists(f"currency_dfs/{curr[0]}/fx_daily_{curr[0]}_{row[1]}.csv"):
                        with open(f"currency_dfs/{curr[0]}/fx_daily_{curr[0]}_{row[1]}.csv","w",encoding="UTF8",newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(["date", "currency", "rate"])
                            writer.writerow(row)
                        print(f"W: {day} {curr[0]} {row[1]}")
                    else:
                        with open(f"currency_dfs/{curr[0]}/fx_daily_{curr[0]}_{row[1]}.csv","a",encoding="UTF8",newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(row)
                            f.close()
                        print(f"A: {day} {curr[0]} {row[1]}")
    else:
        print("Today rate has been extracted")


save_csv()
