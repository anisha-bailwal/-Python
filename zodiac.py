#zodiac sign
person={}

person["name"] = input("enter your name:")
person["birth_month"]= input("enter your birth month:").strip().lower()
zodiac ={
    "jan":"capricon/Aquarius",
    "feb":"Aquarius/Pisces",
    "march":"Pisces/Aries",
    "april":"Aries/Taurus",
    "May":"Taurus/Gemini",
    "june": "gemini/Cancer",
    "July": "Cancer/Leo",
    "August":"Leo/Virgo",
    "September":"Virgo/Libra",
    "Oct":"Libra/Scorpio",
    "Nov":"Scorpio/Sagittarius",
    "Dec":"Sagittarius/Capricon"
}

month=person["birth_month"]
if month in zodiac:
    print("\nName:",person["name"])
    print("Birth Month:",month.title())
    print("possible Zodiac Sign(s):",zodiac[month])
else:
    print("Invalid month entered!")    











#relationship detector
# person={}
# person["name"]=input("Enter your name:")
# person["sleep_hours"]= float(input("How many hours do you sleep per day:"))
# person["avoid_time"]=int(input("how many times you tell a lie to your parents daily:"))
# person["phone_hours"]=float(input("How many hours do you spend on your phonecalls daily:"))
# person["chat_hours"]=float(input("How many hours do you spend chatting daily:"))
# person["selfies_per_week"]=int(input("How many selfies do you take per week:"))
# person["late_night_awake"]= input("Do you stay awake after midnight?(yes/no):").lower

# score =0
# #fun scoring rules
# if person["phone_hours"]>5:
#     score=+2
# if person["chat_hours"]>2:
#     score=+3
# if person["selfies_per_week"]>10:
#     score=+1
# if person["late_night_awake"]=="yes":
#   score=+2
# if person["sleep_hours"]<6:
#   score=+1
# if person["avoid_time"]>2:
#    score=+1   
# # Determining Status
# if score<=5:
#    status="you are single"
# elif score<=9:
#    status ="YOu have a crush"
# else:
#    status ="You are committed"

# print("\n--------RESULT---------\n")  
# print("Name:",person["name"])
# print("Relationship Prediction:",status)                     
