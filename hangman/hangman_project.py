# Write your code below this line
#program to create a game of HANGMAN
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
word_list=["ardwark","baboon","camel"]
chosen_word=random.choice(word_list)
print(f"PSSST!The chosen word is {chosen_word}")
l=[]
for letter in chosen_word:
  l+="_"
while("_" in l):
    guess=input("Please enter a letter")
    guess=guess.lower()
    flag=0
    for i in range(0,len(chosen_word)):
        if chosen_word[i]==guess:
            flag=1
            l[i]=guess
            print(l)
    if(flag==0):    
        print(stages[lives])
        lives=lives-1
        if lives==-1:
            print("ALL LIVES ARE OVER!YOU LOSE")





