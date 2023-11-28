text = input ("Enter name of Variable ")
new_text = ""
for i in range(len(text)):
    if i == 0:
        if text[0].isupper() == True:
            new_text = text[0].lower()
        else:
            new_text = text[0]
    elif text[i].isupper() == True:
        new_text = new_text + "_" + text[i].lower()
    else:
        new_text = new_text + text[i]
print (new_text)
