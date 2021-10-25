import os
import csv
import requests
import bs4 as bs

def save_csv():
    curr_list = [["AED","Emirati Dirham"],
                 ["ARS","Argentine Peso"],
                 ["AUD","Australian Dollar"],
                 ["BGN","Bulgarian Lev"],
                 ["BHD","Bahraini Dinar"],
                 ["BND","Bruneian Dollar"],
                 ["BRL","Brazilian Real"],
                 ["BWP","Botswana Pula"],
                 ["CAD","Canadian Dollar"],
                 ["CHF","Swiss Franc"],
                 ["CLP","Chilean Peso"],
                 ["CNY","Chinese Yuan Renminbi"],
                 ["COP","Colombian Peso"],
                 ["CZK","Czech Koruna"],
                 ["DKK","Danish Krone"],
                 ["EUR","Euro"],
                 ["GBP","British Pound"],
                 ["HKD","Hong Kong Dollar"],
                 ["HRK","Croatian Kuna"],
                 ["HUF","Hungarian Forint"],
                 ["IDR","Indonesian Rupiah"],
                 ["ILS","Israeli Shekel"],
                 ["INR","Indian Rupee"],
                 ["IRR","Iranian Rial"],
                 ["ISK","Icelandic Krona"],
                 ["JPY","Japanese Yen"],
                 ["KRW","South Korean Won"],
                 ["KWD","Kuwaiti Dinar"],
                 ["KZT","Kazakhstani Tenge"],
                 ["LKR","Sri Lankan Rupee"],
                 ["LYD","Libyan Dinar"],
                 ["MUR","Mauritian Rupee"],
                 ["MXN","Mexican Peso"],
                 ["MYR","Malaysian Ringgit"],
                 ["NOK","Norwegian Krone"],
                 ["NPR","Nepalese Rupee"],
                 ["NZD","New Zealand Dollar"],
                 ["OMR","Omani Rial"],
                 ["PHP","Philippine Peso"],
                 ["PKR","Pakistani Rupee"],
                 ["PLN","Polish Zloty"],
                 ["QAR","Qatari Riyal"],
                 ["RON","Romanian New Leu"],
                 ["RUB","Russian Ruble"],
                 ["SAR","Saudi Arabian Riyal"],
                 ["SEK","Swedish Krona"],
                 ["SGD","Singapore Dollar"],
                 ["THB","Thai Baht"],
                 ["TRY","Turkish Lira"],
                 ["TTD","Trinidadian Dollar"],
                 ["TWD","Taiwan New Dollar"],
                 ["USD","US Dollar"],
                 ["VEF","Venezuelan Bolivar"],
                 ["ZAR","South African Rand"]]
    
    for curr in curr_list:
        src = requests.get(f"https://www.x-rates.com/table/?from={curr[0]}&amount=1")
        soup = bs.BeautifulSoup(src.text, "lxml")
        table = soup.find("table", {"class": "tablesorter ratesTable"})
        currs = []
        
        for row in table.findAll("tr")[1:]:
            currency = row.findAll("td")[0].text
            for abbv in curr_list:
                if currency==abbv[1]: currency=abbv[0]
            exchange = row.findAll("td")[1].find('a').contents[0]
            currs.append([currency,exchange])

        with open(f"currency_dfs/{curr[0]}_exchange.csv","w",encoding="UTF8",newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["currency", "rate"])
            for exc in currs:
                writer.writerow(exc)

save_csv()
