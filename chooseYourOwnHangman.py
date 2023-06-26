# importing modules and files
import random
import art
import words

# setting up variables needed for  hangman
# word_list = words.word_list
# chosen_word = random.choice(word_list)
# end_of_game = False
# lives = 6
# stages = art.stages
logo = art.logo
# guessed_letters = []
# display = []



# printing logo for game
print(f"{logo}\n")

print("\nWelcome to Hangman's Jungle.")
print("Your mission is to leave with your head on your shoulders.")

choice1 = input('You\'ve reached a fork in the road. Type "left" or "right"  ')

if choice1 == "left":
    choice11 = input("You come to Lake WaterHole. Choose one: Swim or Wait ")


if choice1 == "right":
    print("You run into a Big Mo, Mesquito King of the Jungle. Its time to play hangman")

# start of hangman logic
    # setting up variables needed for  hangman
    word_list = words.word_list
    chosen_word = random.choice(word_list)
    end_of_game = False
    lives = 6
    stages = art.stages
    guessed_letters = []
    display = []

    #Testing code
    print(f'Pssst, the solution is {chosen_word}.')


    #Creating blanks for display
    display = []

    for letter in chosen_word:
        display.append("_")


    print(stages[lives])
    print(f"{' '.join(display)}")

    #While loop to keep the user guessing until completed
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # clear()

        if guess in display:
            print(f"Nice try Grandma but dont you remember you already guessed '{guess}'. Try again.")

        # checks if the  user guessedright and switches the blank with the letter if it was correct
        i = 0
        for letter in chosen_word:
            if letter == guess:
                display[i] = guess

            i += 1

        #Checks if guess was wrong and detreacts from their life score if so.
        if guess not in chosen_word:
            print(f"You guessed '{guess}'. That was a foolish answer. You lose a life.")
            lives -= 1
            # Checks if user still has life if not game over
            if lives == 0:
                end_of_game = True
                print("You lose, loser.")



        # prints the display list variable as a string
        print(f"{' '.join(display)}")


        # checks if user has guessed all the blanks and if so wins
        if "_" not in display:
            end_of_game = True
            print("You've won.")

        print(stages[lives])
# end of hangman logic
