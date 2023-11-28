import emoji

def main():
    x = function()
    print (x)

def function():
    prompt = input ("Input: ")
    prompt = emoji.emojize(prompt)
    return prompt

if __name__ == "__main__":
    main()