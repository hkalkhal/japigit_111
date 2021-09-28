import urllib.request
import json


def getStockData(symb):
    link="https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+symb+"&interval=5min&apikey=S05HRL7UDDM0QATA"
    with urllib.request.urlopen(link) as url:
        s = url.read()
        return s

def main():
    symbol = input("Enter stock symbol: ")
    while(symbol != "quit"):
        result = getStockData("TSLA")
        print(result)
        data = json.loads(result)
        with open('japi.out', 'w') as f:
            json.dump(data, f)
        print("The current price of " + symbol + " is: " + data['Global Quote']['05. price'])
	print("Stock quotes retrieved successfully!")
        symbol = input("Enter stock symbol: ")

main()