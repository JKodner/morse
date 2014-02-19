import os, pygame, time
morse = {
"a": "o-", "b": "-ooo", "c": "-o-o", "d": "-oo", "e": "o", "f": "oo-o", "g": "--o", "h": "oooo", "i": "oo",
"j": "o---", "k": "-o-", "l": "o-oo", "m": "--", "n": "-o", "o": "---", "p": "o--o", "q": "--o-", "r": "o-o",
"s": "ooo", "t": "-", "u": "oo-", "v": "ooo-", "w": "o--", "x": "-oo-", "y": "-o--", "z": "--oo", 1: "o----",
2: "oo---", 3: "ooo--", 4: "oooo-", 5: "ooooo", 6: "-oooo", 7: "--ooo", 8: "---oo", 9: "----o",
0: "-----", " ": "/"
}
os.system('clear')
phrase = raw_input("What Phrase Do You Want Converted Into Morse Code?")
char_list = []
foo = []
result = " "
for i in phrase:
    try:
        i = int(i)
    except ValueError:
        None
    char_list.append(i)
for i in char_list:
    if str(i).isalpha():
        result += morse[i.lower()] + " "
    else:
        if i in morse:
            result += morse[i] + " "
        else:
            result += i + " "
os.system('clear')
print result
pygame.init()
for i in result:
    if i == "o":
        pygame.mixer.Sound('/Users/jacobkodner/Downloads/beep-7.wav').play()
        time.sleep(0.1)
    elif i == "-":
        pygame.mixer.Sound('/Users/jacobkodner/Downloads/beep-8.wav').play()
        time.sleep(0.3)