import sys

def main():
    x = 0
    if len(sys.argv) < 2:
        sys.exit ("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit ("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit ("Not a Python file")
        else:
            try:
                f = open (sys.argv[1],"r")
                lines = (f.readlines())
                for line in lines:
                    if line.lstrip().startswith("#"):
                        pass
                    elif line.isspace():
                        pass
                    else:
                        x += 1
                print (x)
            except FileNotFoundError:
                sys.exit ("File does not exist")

if __name__ == "__main__":
    main()
#f = open("demofile.txt", "r")
#print(f.readlines())