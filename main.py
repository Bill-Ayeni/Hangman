import random
from wordlist import words
from men import stages

todays_word = random.choice(words)
display = []

for letter in todays_word:
    display+="_"
print(display)

user_life = 6
guess_list = []
while "_" in display and user_life > 0:
    userinput = input("Guess a letter ")
    userinput1 = userinput.lower()

    for position in range(len(todays_word)):
        if userinput1 == todays_word[position]:
            display[position] = todays_word[position]
            print(userinput1)
   
    if userinput1 in guess_list:
        print(f"You have used that letter. {user_life} lives remaining")
    elif userinput1 not in todays_word:
        user_life -= 1
        print(f"{userinput1} is not in the word. {user_life} lives remaining")    
    guess_list += userinput1
   
    if user_life == 0:
        print(stages[0])
        print("Lose")
    print(display)   
    if user_life == 6:
        print(stages[6])
    elif user_life == 5:
        print(stages[5])
    elif user_life == 4:
        print(stages[4])
    elif user_life == 3:
        print(stages[3])
    elif user_life == 2:
        print(stages[2])
    elif user_life == 1:
        print(stages[1])

    if "_" not in display:
        print("WIN")

print(f"{' '.join(display)}")
