
# Generate the multiplication table for 1 to 10 times that number and ask each math fact as a question (psst...that's a hint).
# If the user gets the math correct, award them a point. If they get it wrong, do not give them any points.
# At the end of the 10 rounds, show the user their score out of 10 for how many math facts they got correct.
# Why not give users an emoji if they get all 10 math facts correct?

print("Welcome to Math Facts Game")
print()
print("How well do you know your math facts? Pick a number and I will give you 10 math facts to solve.")
print()

fact_family = int(input("Name your multiples: "))
print()

counter = 0
for i in range(1, 11):
  correct_answer = i*fact_family
  print(i, "x", fact_family)
  answer = int(input("> "))
  if answer == correct_answer:
    print("You got it right!")
    counter += 1
  else:
    print("That's not correct. It should have been", correct_answer)

if counter == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", counter, "out of 10 correct.")





    
    