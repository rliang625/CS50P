def fuel():
    answer = convert()
    print (answer)

def convert():
    while True:
        try:
            prompt = (input("Enter fraction. "))
            num, dem = (prompt.split ("/"))
            num = int(num)
            dem = int (dem)
            if num > dem:
                raise ValueError
            x = round(num/dem*100)
            break
        except (ValueError, ZeroDivisionError):
            continue
    if x >= (99):
        return ("F")
    elif x <= (1):
        return ("E")
    else:
        return (str(x)+"%")

fuel()


