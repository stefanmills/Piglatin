import pprint
print("This is a program to do some word count for you.")
print("="*50)
sentence=input()
count={}

for character in sentence.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)