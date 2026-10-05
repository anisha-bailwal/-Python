# Zodiac Sign Finder

person = {}
person["name"] = input("Enter your name: ")
day = int(input("Enter your birth date (1-31): "))
month = input("Enter your birth month: ").strip().lower()

# Zodiac ranges (month, day)
zodiac_ranges = [
    ("capricorn", (12, 22), (1, 19)),
    ("aquarius", (1, 20), (2, 18)),
    ("pisces", (2, 19), (3, 20)),
    ("aries", (3, 21), (4, 19)),
    ("taurus", (4, 20), (5, 20)),
    ("gemini", (5, 21), (6, 20)),
    ("cancer", (6, 21), (7, 22)),
    ("leo", (7, 23), (8, 22)),
    ("virgo", (8, 23), (9, 22)),
    ("libra", (9, 23), (10, 22)),
    ("scorpio", (10, 23), (11, 21)),
    ("sagittarius", (11, 22), (12, 21))
]

# Month mapping
month_map = {
    "january": 1, "jan": 1,
    "february": 2, "feb": 2,
    "march": 3, "mar": 3,
    "april": 4, "apr": 4,
    "may": 5,
    "june": 6, "jun": 6,
    "july": 7, "jul": 7,
    "august": 8, "aug": 8,
    "september": 9, "sep": 9,
    "october": 10, "oct": 10,
    "november": 11, "nov": 11,
    "december": 12, "dec": 12
}

if month in month_map:
    m = month_map[month]
    zodiac_sign = None
    for sign, (start_m, start_d), (end_m, end_d) in zodiac_ranges:
        if (m == start_m and day >= start_d) or (m == end_m and day <= end_d):
            zodiac_sign = sign
            break
    
    if zodiac_sign:
        print("\nName:", person["name"])
        print("Birth Date:", day, month.title())
        print("Zodiac Sign:", zodiac_sign.capitalize())
    else:
        print("Invalid date entered!")
else:
    print("Invalid month entered!")
