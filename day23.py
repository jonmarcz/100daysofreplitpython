def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)


rollDice()


# Below we add a range and roll the dice 100 times.
for i in range(100):
  rollDice()

# Challenge below
# create a subroutine (function) with both a username and a password
# create a loop to prompt the user again and again until they put in the correct login information
def getinfo():
    print()
    print("Login System")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    while True:
      checkuser = input("What is your username? ")
      passcheck = input("What is your password? ")
      if checkuser != username:
         print("Please enter a valid username: ")
         continue
      elif passcheck != password:
         print("Please enter a valid password. ")
         continue
      else:
         print("Welcome. ")
         break

# below we have two ways to use the function above. One way is assigning it into a variable
# or also simply putting the name with paranthesis. 
info = getinfo()





