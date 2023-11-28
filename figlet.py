from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        f = figlet.getFonts()[random.randrange(0,len(figlet.getFonts()))]
        figlet.setFont(font=f)
        prompt = input ("Enter text here: ")
        print (figlet.renderText(prompt))
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            try:
                figlet.setFont(font = sys.argv[2])
                prompt = input ("Enter text here: ")
                print (figlet.renderText(prompt))
            except ValueError:
                sys.exit("Invalid Usage")
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

if __name__ == "__main__":
    main()

