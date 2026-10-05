import random
options=["rock","paper","scissors"]
print("ROCK PAPER SCISSORS GAME\n 🪨 vs 📄 vs ✂️")
print("choose one from :\n","rock🪨 \n","paper📄\n","scissors ✂️\n")
while True:
  your_choice=input("enter your choice:")
  computer_choice=random.choice(options)
  print("Computer's move:",computer_choice)
  if computer_choice=="paper" :
    if your_choice=="scissors":
     print("Scissor ✂️ cut paper📄!.You Won")
    elif your_choice=="rock":
       print("Paper📄 wraps rock🪨. /n you lost!")
    elif your_choice=="paper":
       print("both made same choices! its a tie!") 
  elif computer_choice=="rock":
   if your_choice=="scissors":
         print("rock🪨 breaks scissor ✂️! You Lost!")
   elif your_choice=="rock":
       print("both made same choice.Its atie!")
   elif your_choice=="paper":
       print(" Paper📄 wraps rock🪨. You Won!")
  elif computer_choice=="scissors":
       if your_choice=="scissors":
         print("both made same choice.Its atie!")
       elif your_choice=="rock":
         print("rock🪨 breaks scissor ✂️. You Won!")
       elif your_choice=="paper":
        print("Scissors ✂️ cut paper📄.You lost!") 
  else:
   print("You made an invalid choice")
  a=input("Enter Yes if you want to continue to play!:")
  if a=="yes":
    continue
    print()
  else :
    break