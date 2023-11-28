def main():
  x = convert()
  print (x)

months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def convert():
    while True:
        try:
            prompt = input("Year? ")
            if "/" in prompt:
                month,day,year = prompt.split("/")
                if int(month) >12:
                    raise ValueError
                elif int(day) >31:
                    raise ValueError
                if int(month)<10:
                    month = f"{int(month):02}"
                if int(day)<10:
                    day = f"{int(day):02}"
                return (year.strip() + "-" + month + "-" + day)
            elif " " in prompt:
                month,day,year = prompt.split(" ")
                day = f"{int(day[:-1]):02}"
                month = f"{int(months.index(month) + 1):02}"
                if int(day) >31:
                    raise ValueError
                return (year.strip() + "-" + month + "-" + day)
        except ValueError:
            continue

main()