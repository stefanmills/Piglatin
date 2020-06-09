#piglatin: a form of encryption

#declaration of variable
vowel=("a","e","i","o","u")

print("WELCOME TO MY PIGLATIN PROGRAM.")
print("="*30)

theword=input("Please input a word\n")

def piglatin(theword):
    if theword.startswith(vowel):
        word= theword+"way"
        print("The piglatin of \""+theword+"\" is "+ word)

    elif theword[0] and theword[1] not in vowel and str:
        word=theword[2:len(theword)]+theword[0]+theword[1]+"ay"
        print("The piglatin of \" "+theword+"\" is "+ word)
    elif theword[0]not in vowel and theword[1] in vowel and str:
        word=theword[1:len(theword)]+theword[0]+"ay"
        print("The piglatin of \" "+theword+"\" is "+ word)
    else:
        print("Please start your word with a letter")

piglatin(theword)