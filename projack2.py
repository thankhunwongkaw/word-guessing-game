"""from english_words import english_words_list
import random
word = list(english_words_set)
choword = word[random.randint(0,len(word))]

chowlist = list(choword)
bla = []
for i in range(len(chowlist)):
    bla.append("_")
bla[0] = chowlist[0]
print(bla)
print("you have 5 guesses")
for i in range(5):
    print(bla)
    e = input("what will be your guess? only one character tho")
    if len(e !=1):
        continue
    if e in chowlist:
        print(e," is in the word!!")
        bla[chowlist.index(e)] = e
    else:
        print(e , "is not in the word")
print("can you confirm your awnser by each character?")
for i in range(len(chowlist)):
    ee = input(f"{i+1} character: ")
    bla[i] = ee
if bla == chowlist:
    print("you got it right!!! the word is" , choword)
else:
    print("the word is" , choword)
    print("your guess is " , bla)
    
"""

import nltk
from nltk.corpus import words
import random

nltk.download('words')

word_list = words.words()
choword = random.choice(word_list)

chowlist = list(choword)
bla = ["_"] * len(chowlist)
bla[0] = chowlist[0]

print(bla)
print("You have 5 guesses")

for _ in range(5):
    print(bla)
    e = str(input("What will be your guess? Only one character though: "))

    if len(e) != 1:
        continue

    if e in chowlist:
        print(e, "is in the word!!")
        indices = [i for i, letter in enumerate(chowlist) if letter == e]
        for idx in indices:
            bla[idx] = e
    else:
        print(e, "is not in the word")
print(bla)
print("Can you confirm your answer by each character?")
for i, letter in enumerate(chowlist):
    ee = str(input(f"{i + 1} character: "))
    bla[i] = ee
    print(bla)

if bla == chowlist:
    print("You got it right!!! The word is", choword)
else:
    print("The word is", choword)
    print("Your guess is", bla)