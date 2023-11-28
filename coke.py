total = 50
print("Amount Due: ", total)
while total > 0:
        money = input ("Insert Coin ")
        if int(money) == 25:
            total = total - 25
            if total >= 0:
                print ("Amount Due ",total)
            else:
                print ("Change Owed ", abs(total))
        elif int(money) == 10:
            total = total - 10
            if total >= 0:
                print ("Amount Due ",total)
            else:
                print ("Change Owed ", abs(total))
        elif int(money) == 5:
            total = total - 5
            if total >= 0:
                print ("Amount Due ",total)
            else:
                print ("Change Owed ", abs(total))
        else:
            print (total)
