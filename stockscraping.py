# Software Developer:   Tevin Gladden
# Date              :   11/27/2019
# Project Name      :   FinViz Stock Scraper


# The program extracts data related to stocks when a stock symbol is manually inputted.
# The data extracted is then written into a CSV File to be used for Day Trading purposes.
# All data is acquired from finviz.com, a financial website providing updated stock data for
# all traders to use in their endeavors.
#
#   Inputs: Stock Symbol
#           -   Stock: Facebook
#           -   Symbol: FB
#   Outputs: CSV file with the following features
#           -   Shares Outstanding
#           -   Market Capital
#           -   Shares Float
#           -   Average Volume
#
# The execution of this program may end by entering "quit" at the request of a new stock
# symbol.
#

import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup


flag = True
values = ["Shs Outstand", "Market Cap", "Shs Float", "Avg Volume"]
csvOutput = [["Stock Symbol", "Outstanding Shares", "Market Capital", "Shares Float", "Average Volume"]]
temp = []
table = {}
url = 'https://finviz.com/quote.ashx?t='
symbol = input("Enter the stock symbol of the stock you "
                         "wish to pull data from: ").upper()
while symbol != "QUIT":

    print("Extracting data from ", url+symbol,"\n\n")
    response = requests.get(url+symbol)
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.select('.table-dark-row')

    for post in posts:
        for td in post.find_all("td"):
            temp.append(td.get_text())

    table["Symbol"] = symbol

    for i in range(len(temp)):
        if temp[i] in values:
            table[temp[i]] = temp[i+1]
    print(table,"\n")
    csvOutput.append(list(table.values()))
    print(csvOutput, "\n")

    symbol = input("Enter quit to end or Enter the stock symbol of the stock you "
                         "wish to pull data from: ").upper()
    print("\n")

with open('newStockData.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvOutput)

df = pd.DataFrame(csvOutput[1:], columns=csvOutput[0])
print(df)

