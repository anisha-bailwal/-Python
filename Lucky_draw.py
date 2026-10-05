import getpass
import random
members=['Aman','Aanchal','Anisha','Avneesh','arshi']
winner=random.choice(members)
print(f"todays winner is:{winner}")
print("you have maximum two chances to win")
number=int(getpass.getpass("My lucky number is:"))
count=1
chances=3
while count<chances:
        guess=int(input(f"number entered by {winner}:"))
        count+=1
        if guess==number:
                print(f"Congratulations {winner} you have won the game")
                break
        else:
                print("try again")
print(f"The lucky number was{number}")
