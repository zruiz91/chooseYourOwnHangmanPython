# importing modules and files
#HINT: You can call clear() to clear the output in the console.
from replit import clear
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
death = art.death
cheers = art.beer
boat = art.boat
forest = art.forest
lighter = art.lighter
fairy = art.fairy
skull = art.skull
treasure = art.treasure
butt = art.butt
fork_in_road = art.fork_in_road
seabeast = art.seabeast
boat = art.boat
lake_waterhole = art.lake_waterhole
seabeast = art.seabeast
smoking = art.smoking

# !!!!!!!!!!! Preamble for the game !!!!!!!!!!!!!!!!!!!
# printing logo for game
print(f"{logo}\n")

print("\nWelcome to Hangman's Jungle.")

# user inputs name
user_name = input("\nType your name here:  ")

clear()
print(forest)
print(f"\nOnce upon a time, deep within the heart of the enchanted forest, there was a brave adventurer named {user_name}. As they ventured through the dense woods, they stumbled upon a weathered map that depicted the location of a mythical treasure hidden within the forest.\n")

input("click Enter to continue")

clear()
print(treasure)
print(f"Driven by curiosity and a thirst for adventure, {user_name} decided to embark on a journey to uncover the treasure.")
print(butt)
input("click Enter to continue")

clear()
print(fairy)
print(f"However, the forest was not only home to beautiful creatures but also dangerous monsters and fierce dragons. {user_name} knew that each step could lead to peril or glory.")
print(skull)
input("click Enter to continue")
clear()
# !!!!!!!!!!! End of Preamble for the game !!!!!!!!!!!!!!!!!!!


# !!!!!!!!!!! First Choice!!!!!!!!!!!!!!!!!!!

print(fork_in_road)
choice1 = input('You\'ve reached a fork in the road. Type "left" or "right"  ').lower()


# !!!!!!!!!!! First Choice Left !!!!!!!!!!!!!!!!!!!
if choice1 == "left":
    clear()
    print(lake_waterhole)
    choice2_1 = input("You come to Lake WaterHole. Choose one: Swim or Wait ").lower()


# !!!!!!!!!!! First Choice Left Second Choice Wait !!!!!!!!!!!!!!!!!!!
    if choice2_1 == "wait":
        clear()
        print(boat)
        print("The boat takes you safely to the other side")
        choice2_1_1 = input("You run into a monkey. He looks cute yet mischevious. Do you pet the monkey. Choose one: yes or no  ").lower()
        if choice2_1_1 == "no":
            clear()
            print("You dont pet the monkey. As you pass the monkey you see a knife clutched in his hand. Once out of your sight you hear a blood curdling scream. You dont look back")
            print(fork_in_road)
            choice2_1_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
            if choice2_1_1_1 == "treasure":
                clear()
                print(death)
                print("Game Over you greedy bastard!")
            if choice2_1_1_1 == "exit":
                clear()
                print(cheers)
                print("The end. You escape. You Win. Go Home. It's over")
        if choice2_1_1 == "yes":
            clear()
            print("You pet the monkey he tries to steal your soul. To fend him off you must play hangman")

                            # !!!!!!!!!!!!!!!! Start of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            # setting up variables needed for  hangman
            word_list2_1_1 = words.word_list
            chosen_word2_1_1 = random.choice(word_list2_1_1)
            end_of_game2_1_1 = False
            lives2_1_1 = 6
            stages2_1_1 = art.stages
            guessed_letters2_1_1 = []
            display2_1_1 = []

            #Testing code
            print(f'Pssst, the solution is {chosen_word2_1_1}.')
            #Creating blanks for display
            # display = []

            for letter in chosen_word2_1_1:
                display2_1_1.append("_")

            print(stages2_1_1[lives2_1_1])
            print(f"{' '.join(display2_1_1)}")

            #While loop to keep the user guessing until completed
            while not end_of_game2_1_1:
                guess2_1_1 = input("Guess a letter: ").lower()

                # clear()

            if guess2_1_1 in display2_1_1:
                print(f"Nice try Grandma but dont you remember you already guessed '{guess2_1_1}'. Try again.")

            # checks if the  user guessedright and switches the blank with the letter if it was correct
            i2_1_1 = 0
            for letter in chosen_word2_1_1:
                if letter == guess2_1_1:
                    display2_1_1[i2_1_1] = guess2_1_1

                i2_1_1 += 1

            #Checks if guess was wrong and detreacts from their life score if so.
            if guess2_1_1 not in chosen_word2_1_1:
                print(f"You guessed '{guess2_1_1}'. That was a foolish answer. You lose a life.")
                lives2_1_1 -= 1
                # Checks if user still has life if not game over
                if lives2_1_1 == 0:
                    end_of_game2_1_1 = True
                    print(death)
                    print("You lose, loser.")

            # prints the display list variable as a string
            print(f"{' '.join(display2_1_1)}")

            print(stages2_1_1[lives2_1_1])

            # checks if user has guessed all the blanks and if so wins
            if "_" not in display2_1_1:
                end_of_game2_1_1 = True
                print(cheers)
                print("You've won. for now...")

                                # !!!!!!!!!!!!!!!! End of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                print(fork_in_road)
                choice2_1_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                if choice2_1_1_1 == "treasure":
                    clear()
                    print(death)
                    print("Game Over you greedy bastard!")
                if choice2_1_1_1 == "exit":
                    clear()
                    print(cheers)
                    print("The end. You escape. You Win. Go Home. It's over")


# !!!!!!!!!!! First Choice Left Second Choice swim !!!!!!!!!!!!!!!!!!!
    if choice2_1 == "swim":
        clear()
        print(seabeast)
        print("Beast from the depths request 3.50 to pass. You have no money so are forced to play Hangman")

                        # !!!!!!!!!!!!!!!! Start of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # setting up variables needed for  hangman
        word_list2_1 = words.word_list
        chosen_word2_1 = random.choice(word_list2_1)
        end_of_game2_1 = False
        lives2_1 = 6
        stages2_1 = art.stages
        guessed_letters2_1 = []
        display2_1 = []


        #Testing code
        print(f'Pssst, the solution is {chosen_word2_1}.')
        #Creating blanks for display
        # display = []

        for letter in chosen_word2_1:
            display2_1.append("_")


        print(stages2_1[lives2_1])
        print(f"{' '.join(display2_1)}")

        #While loop to keep the user guessing until completed
        while not end_of_game2_1:
            guess2_1 = input("Guess a letter: ").lower()

            # clear()

            if guess2_1 in display2_1:
                print(f"Nice try Grandma but dont you remember you already guessed '{guess2_1}'. Try again.")

            # checks if the  user guessedright and switches the blank with the letter if it was correct
            i2_1 = 0
            for letter in chosen_word2_1:
                if letter == guess2_1:
                    display2_1[i2_1] = guess2_1

                i2_1 += 1

            #Checks if guess was wrong and detreacts from their life score if so.
            if guess2_1 not in chosen_word2_1:
                print(f"You guessed '{guess2_1}'. That was a foolish answer. You lose a life.")
                lives2_1 -= 1
                # Checks if user still has life if not game over
                if lives2_1 == 0:
                    end_of_game2_1 = True
                    print(death)
                    print("You lose, loser.")


            # prints the display list variable as a string
            print(f"{' '.join(display2_1)}")

            print(stages2_1[lives2_1])

            # checks if user has guessed all the blanks and if so wins
            if "_" not in display2_1:
                end_of_game2_1 = True
                print(cheers)
                print("You've won. for now...")


                                # !!!!!!!!!!!!!!!! End of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                clear()
                choice2_1_1 = input("You run into a monkey. He looks cute yet mischevious. Do you pet the monkey. Choose one: yes or no  ").lower()
                if choice2_1_1 == "no":
                    clear()
                    print("You dont pet the monkey. As you pass the monkey you see a knife clutched in his hand. Once out of your sight you hear a blood curdling scream. You dont look back")
                    print(fork_in_road)
                    choice2_1_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                    if choice2_1_1_1 == "treasure":
                            clear()
                            print(death)
                            print("Game Over you greedy bastard!")
                    if choice2_1_1_1 == "exit":
                            clear()
                            print(cheers)
                            print("The end. You escape. You Win. Go Home. It's over")
                if choice2_1_1 == "yes":
                    clear()
                    print("You pet the monkey he tries to steal your soul. To fend him off you must play hangman")

                                    # !!!!!!!!!!!!!!!! Start of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                    # setting up variables needed for  hangman
                    word_list2_1_1 = words.word_list
                    chosen_word2_1_1 = random.choice(word_list2_1_1)
                    end_of_game2_1_1 = False
                    lives2_1_1 = 6
                    stages2_1_1 = art.stages
                    guessed_letters2_1_1 = []
                    display2_1_1 = []

                    #Testing code
                    print(f'Pssst, the solution is {chosen_word2_1_1}.')
                    #Creating blanks for display
                    # display = []

                    for letter in chosen_word2_1_1:
                        display2_1_1.append("_")

                    print(stages2_1_1[lives2_1_1])
                    print(f"{' '.join(display2_1_1)}")

                    #While loop to keep the user guessing until completed
                    while not end_of_game2_1_1:
                        guess2_1_1 = input("Guess a letter: ").lower()

                        # clear()

                        if guess2_1_1 in display2_1_1:
                            print(f"Nice try Grandma but dont you remember you already guessed '{guess2_1_1}'. Try again.")

                        # checks if the  user guessedright and switches the blank with the letter if it was correct
                        i2_1_1 = 0
                        for letter in chosen_word2_1_1:
                            if letter == guess2_1_1:
                                display2_1_1[i2_1_1] = guess2_1_1

                            i2_1_1 += 1

                        #Checks if guess was wrong and detreacts from their life score if so.
                        if guess2_1_1 not in chosen_word2_1_1:
                            print(f"You guessed '{guess2_1_1}'. That was a foolish answer. You lose a life.")
                            lives2_1_1 -= 1
                            # Checks if user still has life if not game over
                            if lives2_1_1 == 0:
                                end_of_game2_1_1 = True
                                print(death)
                                print("You lose, loser.")

                        # prints the display list variable as a string
                        print(f"{' '.join(display2_1_1)}")

                        print(stages2_1_1[lives2_1_1])


                        # checks if user has guessed all the blanks and if so wins
                        if "_" not in display2_1_1:
                            end_of_game2_1_1 = True
                            print(cheers)
                            print("You've won. for now...")

                                            # !!!!!!!!!!!!!!!! End of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            print(fork_in_road)
                            choice2_1_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                            if choice2_1_1_1 == "treasure":
                                clear()
                                print(death)
                                print("Game Over you greedy bastard!")
                            if choice2_1_1_1 == "exit":
                                clear()
                                print(cheers)
                                print("The end. You escape. You Win. Go Home. It's over")


# !!!!!!!!!!! First Choice right: Big Mo, Mesquito King !!!!!!!!!!!!!!!!!!!
if choice1 == "right":
    print("You run into a Big Mo, Mesquito King of the Jungle. Its time to play hangman")

                # !!!!!!!!!!!!!!!! Start of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
    # display = []

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
                print(death)
                print("You lose, loser.")



        # prints the display list variable as a string
        print(f"{' '.join(display)}")

        print(stages[lives])
        # checks if user has guessed all the blanks and if so wins
        if "_" not in display:
            end_of_game = True
            print(cheers)
            print("You've won. for now..")

                            # !!!!!!!!!!!!!!!! End of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            print(lighter)
            choice2_1 = input("You find a bag in the road. It has two items in it. Choose one: Lighter or Dictionary").lower()
            print("You run into a giant trying to light a cigarette.")


            if choice2_1 == "lighter":
                print(smoking)
                print("You let him use your lighter and he continues to smoke all his life until one day he gets lung cancer. He dies. You pass ")
                print(fork_in_road)
                choice2_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                if choice2_1_1 == "treasure":
                    clear()
                    print(death)
                    print("Game Over you greedy bastard!")
                if choice2_1_1 == "exit":
                    clear()
                    print(cheers)
                    print("The end. You escape. You Win. Go Home. It's over")

            if choice2_1 == "dictionary":
                print("The giant looks down at you and asks for a light. When you say you dont smoke he becomes infuriated. You throw your dictionary at him in vain. Time to play hangman.")


                # !!!!!!!!!!!!!!!! Start of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                # setting up variables needed for  hangman
                word_list2_1 = words.word_list
                chosen_word2_1 = random.choice(word_list2_1)
                end_of_game2_1 = False
                lives2_1 = 6
                stages2_1 = art.stages
                guessed_letters2_1 = []
                display2_1 = []


                #Testing code
                print(f'Pssst, the solution is {chosen_word2_1}.')
                #Creating blanks for display
                # display = []

                for letter in chosen_word2_1:
                    display2_1.append("_")


                print(stages2_1[lives2_1])
                print(f"{' '.join(display2_1)}")

                #While loop to keep the user guessing until completed
                while not end_of_game2_1:
                    guess2_1 = input("Guess a letter: ").lower()

                    # clear()

                    if guess2_1 in display2_1:
                        print(f"Nice try Grandma but dont you remember you already guessed '{guess2_1}'. Try again.")

                    # checks if the  user guessedright and switches the blank with the letter if it was correct
                    i2_1 = 0
                    for letter in chosen_word2_1:
                        if letter == guess2_1:
                            display2_1[i2_1] = guess2_1

                        i2_1 += 1

                    #Checks if guess was wrong and detreacts from their life score if so.
                    if guess2_1 not in chosen_word2_1:
                        print(f"You guessed '{guess2_1}'. That was a foolish answer. You lose a life.")
                        lives2_1 -= 1
                        # Checks if user still has life if not game over
                        if lives2_1 == 0:
                            end_of_game2_1 = True
                            print(death)
                            print("You lose, loser.")


                    # prints the display list variable as a string
                    print(f"{' '.join(display2_1)}")

                    print(stages2_1[lives2_1])

                    # checks if user has guessed all the blanks and if so wins
                    if "_" not in display2_1:
                        end_of_game2_1 = True
                        print(cheers)
                        print("You've won. for now...")

                        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! end of hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                        choice2_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                        if choice2_1_1 == "treasure":
                            clear()
                            print(death)
                            print("Game Over you greedy bastard!")
                        if choice2_1_1 == "exit":
                            clear()
                            print(cheers)
                            print("The end. You escape. You Win. Go Home. It's over")

