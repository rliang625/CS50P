import random
def main():
    x = number_guesser()
    print (x)

def number_guesser():
    while True:
        try:
            prompt = input("Level: ")
            prompt = int(prompt)
            if prompt <= 0:
                raise ValueError
            break
        except ValueError:
            continue
    number = random.randrange(1, prompt + 1)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                raise ValueError
            elif guess < number:
                print ("Too small!")
            elif guess > number:
                print ("Too large!")
            elif guess == number:
                return ("Just right!")
        except ValueError:
            continue

if __name__ == "__main__":
    main()
