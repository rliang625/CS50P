def convert (x):
    x = x.replace(':)','🙂')
    x = x.replace(':(','🙁')
    print (x)
def main ():
    y = input ("Type text here: ")
    convert (y)
main ()