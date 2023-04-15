import random


print()
print()


# This loop will keep repeating if they do no enter "y" or "n".

def the_whole_game():

    

    while True:
        print("""Can you guess my number between 1 and 1,000,000? 
                Press y to play
                Press n to exit""")
        access = input("> ")
        access = access.lower()
        # If they chose to play, we have a loop so they can keep playing until they get my number right. 
        if access == "y":
            print()
            print("Goodluck! ")
            print()
            while True:
                user_guess = input("Pick your number: ")
                for i in range(1):
                  computer_pick = random.randint(1,1000000)
                  print(f"The computer picked {computer_pick}")
                

                #Making sure they enter a valid number

                if user_guess.isdigit():
                    print(f"You picked {user_guess}. The computers was {computer_pick}")
                    print()

                    # creating conditionals for the user if they get it right or wrong
                    if int(user_guess) == int(computer_pick):
                        print("You got it! Good job. Would you like to play again? ")
                        play_again = input("Type 'y' to play or 'n' to quit. ")
                        play_again = play_again.lower()
                        if play_again == 'y':
                            continue
                        else:
                            break
                    elif int(user_guess) < int(computer_pick):
                        print("Your guess was lower than mine. Would you like to try again? ")
                        play_again = input("Type 'y' to play or 'n' to quit. ")
                        play_again = play_again.lower()
                        if play_again == 'y':
                            continue
                        else:
                            break
                    elif int(user_guess) > int(computer_pick):
                        print("Your number is bigger than mine. Would you like to try again? ")
                    
                else:
                    print("Please enter a valid number. ")
        elif access == "n":
            break
        else:
            print("You must enter a valid entry. ")       
            continue 




    
the_whole_game()