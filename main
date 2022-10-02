import random

# import wordlist.py
# words = wordlist.words1[]

from wordlist import words
from men import stages

#words = ["do", "jump"]

#print(words)

todays_word = random.choice(words)

#print(todays_word)

display = []

for letter in todays_word:
    display+="_"
print(display)

#userinput = input("Guess a letter ")
#userinput1 = userinput.lower()

# user_life = 5
# while user_life > 0 or display.find(_) <= 0:
#     userinput = input("Guess a letter ")
#     userinput1 = userinput.lower()
#     for position in range(len(todays_word)):
#         if userinput1 == todays_word[position]:
#             display[position] = todays_word[position]
#             print(userinput1)
#
#         else:
#             user_life-= 1
#
# print(display)

# user_life = 5
#
# end_of_game = False
# while not end_of_game:
#     userinput = input("Guess a letter ")
#     userinput1 = userinput.lower()
#     for position in range(len(todays_word)):
#         if userinput1 == todays_word[position]:
#             display[position] = todays_word[position]
#             print(userinput1)
#
#     print(display)
#
#     if "_" not in display:
#         end_of_game = True



user_life = 6
guess_list = []
while "_" in display and user_life > 0:
    userinput = input("Guess a letter ")
    userinput1 = userinput.lower()
    # if userinput1 in guess_list:
    #     print("You have used that letter")
    # guess_list += userinput1
    for position in range(len(todays_word)):
        if userinput1 == todays_word[position]:
            display[position] = todays_word[position]
            print(userinput1)
    # if userinput1 in display:
    #     print("you have used that letter")
    if userinput1 in guess_list:
        print(f"You have used that letter. {user_life} lives remaining")
    elif userinput1 not in todays_word:
        user_life -= 1
        print(f"{userinput1} is not in the word. {user_life} lives remaining")
    guess_list += userinput1
        #print(user_life)
    #print(user_life)
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
#     # if "_" not in display:
#     #     end_of_game = True


# user_life = 6
#
# while "_" in display and user_life > 0:
#     userinput = input("Guess a letter ")
#     userinput1 = userinput.lower()
#     for position in range(len(todays_word)):
#         if userinput1 not in todays_word:
#             user_life = user_life - 1
#             print(user_life)
#         elif userinput1 == todays_word[position]:
#             display[position] = todays_word[position]
#             print(user_life)
#     if user_life == 0:
#         print("Lose")
#     print(display)
#
# print(f"{' '.join(display)}")


#Worse way to do it
# position = 0
# for letters in todays_word:
#     if userinput1 == todays_word[position]:
#         print(userinput1)
#     else:
#         print("wrong")
#     position+= 1


# if todays_word.find(userinput1) > 0:
#     print("yup")
# else:
#     print("nope")
