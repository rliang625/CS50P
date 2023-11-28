from tabulate import tabulate
import sys
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit ("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit ("Too many command line arguments")
    elif sys.argv[1].endswith(".csv"):
        try:
            fileTBR = (sys.argv[1])
            with open(fileTBR) as file:
                reader = list(csv.reader(file))
                heading = reader[0]
            print (tabulate(reader[1:], headers = heading,  tablefmt = "grid"))
        except FileNotFoundError:
            sys.exit ("File does not exist")
    else:
        sys.exit ("Not a CSV file")




if __name__ == "__main__":
    main()
