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

choice1 = input('You\'ve reached a fork in the road. Type "left" or "right"  ').lower()

if choice1 == "left":
    choice2_1 = input("You come to Lake WaterHole. Choose one: Swim or Wait ").lower()

    if choice2_1 == "wait":
        print("The boat takes you safely to the other side")
        choice2_1_1 = input("You run into a monkey. He looks cute yet mischevious. Do you pet the monkey. Choose one: yes or no  ").lower()
        if choice2_1_1 == "no":
            print("You dont pet the monkey. As you pass the monkey you see a knife clutched in his hand. Once out of your sight you hear a blood curdling scream. You dont look back")
            choice2_1_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
            if choice2_1_1_1 == "treasure":
                print("Game Over you greedy bastard!")
            if choice2_1_1_1 == "exit":
                print("The end. You escape. You Win. Go Home. It's over")
        if choice2_1_1 == "yes":
            print("You pet the monkey he tries to steal your soul. To fend him off you must play hangman")
            # setting up variables needed for  hangman
            word_list2_1_1 = words.word_list
            chosen_word2_1_1 = random.choice(word_list)
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
                    print("You lose, loser.")

            # prints the display list variable as a string
            print(f"{' '.join(display2_1_1)}")

            # checks if user has guessed all the blanks and if so wins
            if "_" not in display2_1_1:
                end_of_game2_1_1 = True
                print("You've won. for now...")
                # end of hangman logic
                choice2_1_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                if choice2_1_1_1 == "treasure":
                    print("Game Over you greedy bastard!")
                if choice2_1_1_1 == "exit":
                    print("The end. You escape. You Win. Go Home. It's over")



    if choice2_1 == "swim":
        print("Beast from the depths request 3.50 to pass. You have no money so are forced to play Hangman")
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
                    print("You lose, loser.")


            # prints the display list variable as a string
            print(f"{' '.join(display2_1)}")

            # checks if user has guessed all the blanks and if so wins
            if "_" not in display2_1:
                end_of_game2_1 = True
                print("You've won. for now...")
                # end of hangman logic
                choice2_1_1 = input("You run into a monkey. He looks cute yet mischevious. Do you pet the monkey. Choose one: yes or no  ").lower()
                if choice2_1_1 == "no":
                    print("You dont pet the monkey. As you pass the monkey you see a knife clutched in his hand. Once out of your sight you hear a blood curdling scream. You dont look back")
                    choice2_1_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                    if choice2_1_1_1 == "treasure":
                            print("Game Over you greedy bastard!")
                    if choice2_1_1_1 == "exit":
                            print("The end. You escape. You Win. Go Home. It's over")
                if choice2_1_1 == "yes":
                    print("You pet the monkey he tries to steal your soul. To fend him off you must play hangman")
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
                                print("You lose, loser.")

                        # prints the display list variable as a string
                        print(f"{' '.join(display2_1_1)}")


                        # checks if user has guessed all the blanks and if so wins
                        if "_" not in display2_1_1:
                            end_of_game2_1_1 = True
                            print("You've won. for now...")
                            # end of hangman logic
                            choice2_1_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                            if choice2_1_1_1 == "treasure":
                                print("Game Over you greedy bastard!")
                            if choice2_1_1_1 == "exit":
                                print("The end. You escape. You Win. Go Home. It's over")



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
                print("You lose, loser.")



        # prints the display list variable as a string
        print(f"{' '.join(display)}")

        print(stages[lives])
        # checks if user has guessed all the blanks and if so wins
        if "_" not in display:
            end_of_game = True
            print("You've won. for now..")
            # end of hangman logic
            choice2_1 = input("You find a bag in the road. It has two items in it. Choose one: Lighter or Dictionary").lower()
            print("You run into a giant trying to light a cigarette.")


            if choice2_1 == "lighter":
                print("You let him use your lighter and he continues to smoke all his life until one day he gets lung cancer. He dies. You pass ")
                choice2_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                if choice2_1_1 == "treasure":
                    print("Game Over you greedy bastard!")
                if choice2_1_1 == "exit":
                    print("The end. You escape. You Win. Go Home. It's over")

            if choice2_1 == "dictionary":
                print("The giant looks down at you and asks for a light. When you say you dont smoke he becomes infuriated. You throw your dictionary at him in vain. Time to play hangman.")
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
                            print("You lose, loser.")


                    # prints the display list variable as a string
                    print(f"{' '.join(display2_1)}")


                    # checks if user has guessed all the blanks and if so wins
                    if "_" not in display2_1:
                        end_of_game2_1 = True
                        print("You've won. for now...")
                        # end of hangman logic
                        choice2_1_1 = input("You come to a fork in the road One sign says 'treasure'. One sign says 'Exit'. Choose one treasure or sign:  ").lower()
                        if choice2_1_1 == "treasure":
                            print("Game Over you greedy bastard!")
                        if choice2_1_1 == "exit":
                            print("The end. You escape. You Win. Go Home. It's over")

