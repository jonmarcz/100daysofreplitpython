# Let's extend Day 24's project and create a health stats generator for a character in a video game.
def infinitedice():
  import random
  for i in range(1):
    dice_roll = random.randint(1,10)
    print(dice_roll)

def rollboth():
  import random
  for i in range(1):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,8)
    health = roll1 * roll2
    return health


stats = rollboth()

while True:
  print("Welcome warrior! Enter your battletag.")
  
  battletag = input(">")
  print(f"Your health is {stats}")
  
  print("Would you like to generate stats for another character? ")
  anothercharacter = input("Type 'y' for yes or 'n' for no.")
  if anothercharacter == "y":
    continue
  else:
    break