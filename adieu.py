def main():
    final_string = ''
    running_list = []
    while True:
        try:
            if len(running_list) == 0:
                prompt = input ()
                running_list.append(prompt)
            else:
                prompt = input ()
                running_list.append(prompt)
        except EOFError:
            if len(running_list) == 1:
                final_string += running_list[0]
                print (f"Adieu, adieu, to {final_string}")
                break
            elif len(running_list) == 2:
                final_string = running_list[0] + " and " + running_list[1]
                print (f"Adieu, adieu, to {final_string}")
                break
            else:
                final_string += running_list[0]
                for items in (range(1,len(running_list) - 1)):
                    final_string += ", " + running_list[items]
                final_string += ", and " + running_list[-1]
                print (f"Adieu, adieu, to {final_string}")
                break

if __name__ == "__main__":
    main()
