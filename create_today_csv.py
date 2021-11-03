import csv
import requests
import bs4 as bs
import pandas as pd

def save_csv():
    curr_df = pd.read_csv("currency_dfs/physical_currency_list.csv")
    curr_list = [[curr_df["abbv"][i], curr_df["currency"][i]] for i in range(len(curr_df))]

    for curr in curr_list:
        src = requests.get(f"https://www.x-rates.com/table/?from={curr[0]}&amount=1")
        soup = bs.BeautifulSoup(src.text, "lxml")
        table = soup.find("table", {"class": "tablesorter ratesTable"})
        currs = []

        print(src)
        
        for row in table.findAll("tr")[1:]:
            currency = row.findAll("td")[0].text
            for abbv in curr_list:
                if currency==abbv[1]: currency=abbv[0]
            exchange = row.findAll("td")[1].find('a').contents[0]
            currs.append([currency,exchange])

        with open(f"today_dfs/{curr[0]}_exchange.csv","w",encoding="UTF8",newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["currency", "rate"])
            for exc in currs:
                writer.writerow(exc)

save_csv()
