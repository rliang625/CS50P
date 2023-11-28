def main ():
    x = sorted(create_list().items())
    for items, quantity in x:
        print ( quantity, items)

def create_list():
    running_list = {}
    while True:
        try:
            new_item = input().upper()
            if new_item in running_list:
                running_list[new_item] += 1
            else:
                running_list[new_item] = 1
        except EOFError:
            return running_list


main()
