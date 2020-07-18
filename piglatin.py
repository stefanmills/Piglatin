#piglatin: a form of encryption

#declaration of variable
vowel=("a","e","i","o","u")
consonant=("b","c","d","f","g","h","j","k","l",
           "m","n","p","q","r","s","t","v","w","x","y","z")

print("WELCOME TO MY PIGLATIN PROGRAM.")
print("="*30)

theword=input("Please input a word\n")
theword=theword.lower()     #converts the word to lower case.

def piglatin(theword):
    store=""

    #vowel conversion
    if theword.startswith(vowel):
        word=theword+"way"
        print("The piglatin of \""+theword+"\" is "+ word)

    #consonant conversion
    elif theword.startswith(consonant):
        for i in range(0,len(theword)):
            if theword[i] in consonant:
                store= store+theword[i]
            else:
                word=theword[i:len(theword)]+store+"ay"
                print("The piglatin of \""+theword+"\" is "+ word)
                break

piglatin(theword)

