#!/usr/bin/env python3

from datetime import datetime

# Month names mapping
month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December",
}

# Element descriptions
element_descriptions = {
    "AIR": (
        "AIR signs (that's Gemini, Libra, and Aquarius) are the thinkers, "
        "communicators, and doers of the zodiac. They analyze, synthesize, "
        "and probe. They breeze through life, never stopping to catch their breath."
    ),
    "WATER": (
        "WATER signs—Cancer, Scorpio, and Pisces—are known for being sensitive and "
        "sentimental. They tend to hold on to people and items long past their "
        "expiration dates, and their emotions are deep and powerful."
    ),
    "EARTH": (
        "EARTH signs (Taurus, Virgo, and Capricorn) are the most grounded peeps on the "
        "planet—you know, the ones who always keep it one hundred percent real. They're "
        "known to be stable, pragmatic, and unwavering."
    ),
    "FIRE": (
        "FIRE signs (Aries, Leo, Sagittarius) are passionate, dynamic, and temperamental. "
        "They get angry quickly, but they also forgive easily. They are adventurers with "
        "immense energy."
    ),
}

# Get user input
while True:
    try:
        mm = int(input("ENTER the month (1-12): "))
        if 1 <= mm <= 12:
            break
        print("Please enter a valid month (1-12).")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        dd = int(input("ENTER the day (1-31): "))
        if 1 <= dd <= 31:
            break
        print("Please enter a valid day (1-31).")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        yy = input("ENTER the year (YYYY or YY): ").strip()
        if len(yy) == 2:
            # Convert to 1900s or 2000s based on user prompt
            century = input("Were you born in the 2000s? (Yes/No): ").strip().lower()
            if century in ["yes", "y"]:
                year = int("20" + yy)
            else:
                year = int("19" + yy)
        elif len(yy) == 4:
            year = int(yy)
        else:
            print("Please enter a valid year in YY or YYYY format.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid year.")

# Day of week calculation using datetime for accuracy
try:
    birthday = datetime(year, mm, dd)
    dow_name = birthday.strftime("%A")
except ValueError:
    print("Invalid date entered. Please check your inputs.")
    exit(1)

# Zodiac sign calculation
def get_sign(mm, dd):
    if (mm == 1 and dd <= 19) or (mm == 12 and dd > 21):
        return "Capricorn"
    elif (mm == 1 and dd > 19) or (mm == 2 and dd <= 18):
        return "Aquarius"
    elif (mm == 2 and dd > 18) or (mm == 3 and dd <= 20):
        return "Pisces"
    elif (mm == 3 and dd > 20) or (mm == 4 and dd <= 19):
        return "Aries"
    elif (mm == 4 and dd > 19) or (mm == 5 and dd <= 20):
        return "Taurus"
    elif (mm == 5 and dd > 20) or (mm == 6 and dd <= 20):
        return "Gemini"
    elif (mm == 6 and dd > 20) or (mm == 7 and dd <= 22):
        return "Cancer"
    elif (mm == 7 and dd > 22) or (mm == 8 and dd <= 22):
        return "Leo"
    elif (mm == 8 and dd > 22) or (mm == 9 and dd <= 22):
        return "Virgo"
    elif (mm == 9 and dd > 22) or (mm == 10 and dd <= 22):
        return "Libra"
    elif (mm == 10 and dd > 22) or (mm == 11 and dd <= 21):
        return "Scorpio"
    else:
        return "Sagittarius"

def get_element(sign):
    if sign in ["Aries", "Leo", "Sagittarius"]:
        return "FIRE"
    elif sign in ["Gemini", "Libra", "Aquarius"]:
        return "AIR"
    elif sign in ["Cancer", "Scorpio", "Pisces"]:
        return "WATER"
    else:
        return "EARTH"

sign = get_sign(mm, dd)
element = get_element(sign)

print()
print(f"You were born on a {dow_name}.")
print(f"Your sign is {sign}.")
print(f"Your element is {element}.")
print()
print(element_descriptions[element])
