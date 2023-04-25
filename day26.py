# Create a subroutine that rolls a dice of any size and returns that number. -- import random library
def dice_roll():
    import random
   
    roll1 = random.randint(1,7)
    return roll1

# Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.

def double_roll():
    import random
    roll1 = random.randint(1,9)
    roll2 = random.randint(1,7)
    # Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
    stats = roll1*roll2
    return stats


double_roll()
health = double_roll()

# Add a loop to give the user the option to generate health stats for another character.
def main():
    print("Character Health Gnerator")
    print()
    while True:
        name = input("Enter your chracters name: ")
        print(f"Your character has {health} health! Would you like to generate another character?")
        print("Type 'y' for yes and 'n' to exit now. ")
        again = input("> ")
        again.lower()
        if again == "y":
            continue
        else:
            break

main()

