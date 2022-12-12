def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()


string = input().split()
total = ""
for word in string:
    amount = 0
    for letter in word:
        if letter.isalpha():
            amount += 1
    for letter in word:
        if not letter.isalpha():
            total += letter
        else:
            total += sdvig(letter, amount)
    total += " "

print(total)