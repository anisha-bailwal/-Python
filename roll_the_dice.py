import random
def dice_game():
    print("---Welcome to the dice game---")
    members=["Anisha","Aanchal","Arshi","Aman","Avneesh"]
    winner1=random.choice(members)
    winner2=random.choice(members)
    print(f"todays winner are:{winner1} and {winner2}")
    print("--------------------------------------------------")
    print(f"I request {winner1} to come on stage to enter his rollno.")
    print("-------------------------------------------------------------")
    roll1=int(input("Enter your rollno and roll the dice:"))
    print("--------------------------------------------------------------------")
 #player1 Roll
    p1_rolls=[random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    p1_total=sum(p1_rolls)
    print(f"{winner1} rolled {p1_rolls}| Total:{p1_total}")
    print("----------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    #player2
    print(f"I request {winner2} to come on stage to enter his rollno.")
    print("------------------------------------------------------------------")
#player2 roll
    p2_rolls=[random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    p2_total=sum(p2_rolls)
    print(f"{winner2} rolled {p2_rolls}")
    print("----------------------------------------------------------")
    if p1_total>p2_total:
        print("======================================================================")
        print(f"{winner1} wins.")
        print("======================================================================")
    elif p2_total>p1_total:
        print("=========================================================================")
        print(f"{winner2} wins.")
        print("==========================================================================") 
    else:
        print("Result: Its a tie.Oopss!")  
dice_game()                  

             