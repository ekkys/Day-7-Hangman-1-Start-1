# #Step 1 

word_list = ["ardvark", "baboon", "camel"]

# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)

# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess letter: ").lower()
# print(guess)

# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#   if letter == guess:
#     print("Right")
#   else :
#     print("Wrong")


#PRIMITIF METHOD
import random
#TODO-1
# Make a random choice from the list
sum_word = len(word_list) - 1  
print(sum_word)

random_index = random.randint(0, sum_word)
print(random_index)

choosen_word = word_list[random_index]
print(choosen_word)

#TODO-2 Ask the user to guess a letter 
user_guess = input("What do you guess? ").lower()
print(user_guess)

#TODO-3 - Check if the letter the user guessed
for letter in choosen_word:
    print(letter)
  if letter == user_guess :
    print("right")
  else:
    print("wrong")


