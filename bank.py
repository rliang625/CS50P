def payout ():
    text = (input ('Greetings!'  ))
    if text.strip().lower()[0:5] == 'hello':
        print ('$0')
    elif text.strip().lower()[0] == 'h':
        print ('$20')
    else:
        print ('$100')
payout()