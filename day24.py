# We are practicing parameters & arguments
# our function parameters are 'ingredient'
def whichCake(ingredient):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")

# our argument is chocolate
whichCake("chocolate")

# our parameters are ingredients, base, coating
def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")
#function call below followed by function arguments in the paranthesis
whichCake(userIngredient, userBase, userCoating)
import random

  
    

      

# naming our function while also putting our function parameters in the paranthesis
def infinitydice(sides):
  if sides.isdigit():
    newsides = int(sides)
    for i in range(0,newsides):
      roll = random.randint(1,newsides)
      while True:
        print("You rolled", roll)
        print()
        again = input("Would you like to play again? ")
        if again == "yes":
          continue
        else:
          break
      
  else:
   print("Please enter a valid number. ")
  
usersides =  input("How many side? ")



infinitydice(usersides)