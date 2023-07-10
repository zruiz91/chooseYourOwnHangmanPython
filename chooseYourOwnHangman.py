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
# print(butt)
input("click Enter to continue")

clear()
# print(fairy)
print(f"However, the forest was not only home to beautiful creatures but also dangerous monsters and fierce dragons. {user_name} knew that each step could lead to peril or glory.")
print(skull)
input("click Enter to continue")
clear()
# !!!!!!!!!!! End of Preamble for the game !!!!!!!!!!!!!!!!!!!


# !!!!!!!!!!! First Choice!!!!!!!!!!!!!!!!!!!

print(fork_in_road)
choice1 = input("Before you lies a narrow path that splits into two directions. A signpost stands at the crossroads, its inscription worn but readable: Left or Right, the choice is yours.  Choose one: 'left' or 'right' ").lower()


# !!!!!!!!!!! First Choice Left !!!!!!!!!!!!!!!!!!!
if choice1 == "left":
    clear()
    print(lake_waterhole)
    choice2_1 = input("Intrigued by the allure of the unknown, you decide to follow the path to the left. As you venture deeper into the forest, the lush greenery opens up to reveal a sparkling lake, its tranquil waters mirroring the sky above. \n\n However, your progress is halted by the obstacle before you. Will you brave the swim across the lake? (Go to Option 1a) or patiently wait for a boat to arrive?.\n\n Choose one: Swim or Wait ").lower()


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

                clear()

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
        print("Feeling a sense of trepidation, you gather your courage and decide to plunge into the murky depths of the lake, determined to make it to the other side. As you swim further away from the safety of the shore, the water grows eerily still, and an icy chill snakes its way up your spine.\n")
        print("Suddenly, a sinister presence stirs beneath the surface. Dark shadows shift and writhe, and a pair of glowing, malevolent eyes fixate on you. Before you can react, a grotesque creature, born of nightmares, lunges towards you, its jagged teeth gleaming in the pale moonlight.\n")

        print("Panic ensues as you desperately thrash and fight against the monster's vice-like grip. The creature's slimy appendages wrap around your limbs, dragging you deeper into its watery domain. Your heart pounds in your chest as you struggle to break free, gasping for precious air..\n")
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

            clear()

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
                    print("\nOverwhelmed by exhaustion and the creature's relentless assault, you find your strength waning. Your body grows limp as the creature drags you deeper into the murky abyss. The suffocating pressure and the realization of your impending doom weigh heavily on your mind. The last thing you perceive is the creature's wicked grin before all fades into eternal darkness.")


            # prints the display list variable as a string
            print(f"{' '.join(display2_1)}")

            print(stages2_1[lives2_1])

            # checks if user has guessed all the blanks and if so wins
            if "_" not in display2_1:
                end_of_game2_1 = True
                print(cheers)
                print("\nSummoning a surge of adrenaline, you unleash a fierce barrage of punches and kicks upon the creature's vulnerable spots. With each blow, you weaken its grip, causing it to release you. Seizing the opportunity, you propel yourself towards the surface, gasping for air just in the nick of time. Bruised and shaken, you emerge from the water, vowing to continue your quest, now with a heightened sense of caution.")


                                # !!!!!!!!!!!!!!!! End of Hangman logic !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                clear()
                print("\nAs you traverse through the mystical forest, an unexpected encounter awaits you. In a sunlit clearing, you come across a mischievous monkey sitting atop a tree branch, its beady eyes fixated on you. The monkey introduces itself as Chester, the cunning trickster of the forest, known for his notorious pranks and deep knowledge of the enchanted realm. Intrigued by Chester's presence, you decide to engage in conversation.\n")
                print("\nCuriosity piqued, you eagerly ask Chester about his history within the forest. He begins to regale you with tales of his adventures, from outsmarting forest guardians to orchestrating grand heists. The stories are captivating, but a niggling doubt gnaws at the back of your mind.\n")
                choice2_1_1 = input("Do you trust Chester? Choose one: yes or no  ").lower()
                if choice2_1_1 == "no":
                    clear()
                    print("\nDoubt lingers in your mind as you ponder Chester's claims. Determined to uncover the truth, you propose a challenge to Chester, requesting he showcase his legendary trickery. \n")
                    print("Accepting your challenge, Chester sets out to demonstrate his skills. However, as he executes his tricks, a momentary slip exposes his vulnerability. You catch a glimpse of a sadness in his eyes, hinting at a deeper story behind his mischievous facade. Realizing the weight of your suspicions, Chester withdraws into himself, retreating further into the forest, leaving you with lingering questions and a sense of regret.\n")
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
                    print("As you choose to trust Chester's claims, an ominous aura surrounds him. His facade crumbles, revealing his true nature—a malevolent being feeding off fear and despair. ")

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

                        clear()

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
                                print("\nIn a twisted display of power, he ensnares you with dark magic, subjecting you to unimaginable suffering. The forest witnesses your torment as Chester revels in your agony. Broken and defeated, you become a cautionary tale, a reminder of the dangers that lurk within the depths of the enchanted forest.\n")

                        # prints the display list variable as a string
                        print(f"{' '.join(display2_1_1)}")

                        print(stages2_1_1[lives2_1_1])


                        # checks if user has guessed all the blanks and if so wins
                        if "_" not in display2_1_1:
                            end_of_game2_1_1 = True
                            print(cheers)
                            print("\nBut within you, a flicker of resilience remains. Summoning the last reserves of your inner strength, you refuse to succumb to despair. With sheer determination, you tap into the hidden depths of your own magic, countering Chester's dark spells with bursts of light.\n")
                            print("\nAs the battle between darkness and light rages, the forest itself seems to join your side. The trees sway in a symphony of defiance, and mystical creatures emerge, lending their powers to your cause. Together, you mount a ferocious resistance against Chester's malevolence.\n")
                            print("\nAs Chester recoils, weakened and defeated, you seize the opportunity to banish him from the forest forever. With a resounding incantation, you harness the collective magic of the forest, casting him out into a realm of eternal darkness.\n")
                            print("\nBeware, for not everything in the mystical realm is as it seems. In the face of suspicion, the choices you make may lead you down a path of darkness and horror. Trust your instincts, tread carefully, and remember that not all creatures in the forest are to be trusted. Your fate hangs in the balance as you navigate the treacherous depths of this enchanted realm.\n")

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
    print("\nDeep within the heart of the jungle, you find yourself face-to-face with a colossal creature known as Big Mo, the Mesquito King of the Jungle. Towering above you, his wings buzzing with an intimidating energy, Big Mo regards you with a mix of curiosity and hunger. Recognizing the sheer power and danger of Big Mo, you decide to try and forge an alliance. \n")
    print("\nApproaching Big Mo with caution, you attempt to establish a line of communication. \n")
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

        clear()

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
                print("Approaching Big Mo cautiously, you extend an open hand, hoping to convey your peaceful intentions. However, as you draw closer, Big Mo's demeanor changes. The once-docile Mesquito King reveals his true nature—a malevolent force disguised as a guardian.")
                print("\nWithout warning, Big Mo lunges at you, his razor-sharp proboscis seeking to drain your life essence. Panic surges through your veins as you desperately try to defend yourself. However, Big Mo's size and strength overpower you, leaving you defenseless against his relentless onslaught.\n")
                print("\nThe Mesquito King's sinister alliance was merely a ruse, a trap to lure unsuspecting adventurers into his clutches. As your strength wanes and darkness engulfs your vision, you realize the true nature of this forest menace. You become another victim of Big Mo's insatiable thirst for power and dominance.\n")
                print("\nThe jungle mourns the loss of a valiant soul, while Big Mo reigns supreme, his wickedness perpetuating the cycle of fear and darkness. Your journey ends here, a tragic reminder that not all creatures in the forest can be trusted.\n")
                print(death)



        # prints the display list variable as a string
        print(f"{' '.join(display)}")

        print(stages[lives])
        # checks if user has guessed all the blanks and if so wins
        if "_" not in display:
            end_of_game = True
            print(cheers)
            print("\nThrough gestures and a series of non-threatening actions, you convey your peaceful intentions. Surprisingly, Big Mo responds, indicating a desire for a truce. With mutual understanding, you realize that Big Mo's true objective is not dominance, but protection. Together, you form an alliance, with Big Mo acting as a guardian of the jungle and aiding you in future quests.\n")

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

                    clear()

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

