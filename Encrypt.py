"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels"""


def NoVowels(NoVowels):
    CipherText = ""
    for i in NoVowels:
        if ord(i) == 97:
            CipherText = CipherText + ""
        elif i == "e":
            CipherText = CipherText + ""
        elif i == "i":
            CipherText = CipherText + ""
        elif i == "o":
            CipherText = CipherText + ""
        elif i == "u":
            CipherText = CipherText + ""
        else:
            CipherText = CipherText + i
    return CipherText
print (NoVowels('Computer Science Makes the World go round but it doesn\'t make the world round itself!'))





"""Write an encryption code that you make up and run it for the variable NoVowels"""
def trump(donald):
    CipherText = ""
    for i in donald:
        if i == "b":
            CipherText = CipherText + "!"
        elif i == "c":
            CipherText = CipherText + "@"
        elif i == "d":
            CipherText = CipherText + "#"
        elif i == "f":
            CipherText = CipherText + "$"
        elif i == "g":
            CipherText = CipherText + "%"
        elif i == "h":
            CipherText = CipherText + "&"
        elif i == "j":
            CipherText = CipherText + "()"
        elif i == "k":
            CipherText = CipherText + "^"
        elif i == "l":
            CipherText = CipherText + "*"
        elif i == "m":
            CipherText = CipherText + "-"
        elif i == "n":
            CipherText = CipherText + "+"
        elif i == "p":
            CipherText = CipherText + "="
        elif i == "q":
            CipherText = CipherText + "`"
        elif i == "r":
            CipherText = CipherText + "~"
        elif i == "s":
            CipherText = CipherText + "[]"
        elif i == "t":
            CipherText = CipherText + ","
        elif i == "v":
            CipherText = CipherText + "/"
        elif i == "w":
            CipherText = CipherText + "|"
        elif i == "x":
            CipherText = CipherText + "<"
        elif i == "y":
            CipherText = CipherText + ">"
        elif i == "z":
            CipherText = CipherText + "?"
        else:
            CipherText = CipherText + i
    return CipherText
print (trump('Hello. I am president-elect, Donald J. Trump, and we are going to make America Great Again.'))
