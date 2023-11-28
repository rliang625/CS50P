import requests
import sys

def main():
    number = count()
    price = convert(number)
    print(f"${price:,.4f}")

def count():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    return amount

def convert(x):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        print ("Error")
    ratio = (response.json()['bpi']['USD']['rate'])
    lista, listb = ratio.split(",")
    converted_ratio = float(lista + listb)
    final_price = converted_ratio * x
    return final_price

if __name__ == "__main__":
    main()