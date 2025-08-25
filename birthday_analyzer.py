#!/usr/bin/env python

print("ENTER the two-digit month (mm):")
mm=int(input())
print("ENTER the two-digit day (dd):")
dd=int(input())
print("ENTER the two-digit year (yy):")
yy=int(input())

month = {
	  1: "January",
	  2: "February",
	  3: "March",
	  4: "April",
	  5: "May",
	  6: "June",
	  7: "July",
	  8: "August",
	  9: "September",
	10: "October",
	11: "November",
	12: "December",
}

mc = {
	"January": 0,
	"February": 3,
	"March": 3,
	"April": 6,
	"May": 1,
	"June": 4,
	"July": 6,
	"August": 2,
	"September": 5,
	"October": 0,
	"November": 3,
	"December": 5,
}

mc=mc.get(month.get(mm))
		

def dayofbirth(mm, dd, yy, mc):
	dow=(yy + int(yy/4) + mc + dd) % 7
	return dow

def get_dow(dow):
	if dow==0:
	    day="Sunday"
	elif dow==1:
		day="Monday"
	elif dow==2:
		day="Tuesday"
	elif dow==3:
		day="Wednesday"
	elif dow==4:
		day="Thursday"
	elif dow==5:
		day="Friday"
	else:
		day="Saturday"
	return day
	
def get_sign(mm, dd):
	if mm == 1 and dd <= 19:
		sign="Capricorn"
	elif mm == 12 and dd > 20:
		sign="Capricorn"
	elif mm == 1 and dd > 19:
		sign="Aquarius"
	elif mm == 2 and dd <= 18:
		sign="Aquarius"
	elif mm == 2 and dd > 18:
		sign="Pisces"
	elif mm == 3 and dd <= 20:
		sign="Pisces"
	elif mm == 3 and dd > 20:
		sign="Aries"
	elif mm == 4 and dd <= 20:
		sign="Aries"
	elif mm == 4 & dd > 20:
		sign="Taurus"
	elif mm == 5 and dd <= 20:
		sign="Taurus"
	elif mm == 5 and dd > 20:
		sign="Gemini"
	elif mm == 6 and dd <= 21:
		sign="Gemini"
	elif mm == 6 and dd > 21:
		sign="Cancer"
	elif mm == 7 and dd <= 22:
		sign="Cancer"
	elif mm == 7 and dd > 22:
		sign="Leo"
	elif mm == 8 and dd <= 22:
		sign="Leo"
	elif mm == 8 and dd > 22:
		sign="Virgo"
	elif mm == 9 and dd <= 22:
		sign="Virgo"
	elif mm == 9 and dd > 22:
		sign="Libra"
	elif mm == 10 and dd <= 22:
		sign="Libra"
	elif mm == 10 and dd > 22:
		sign="Scorpio"
	elif mm == 11 and dd <= 21:
		sign="Scorpio"
	else:
		sign="Sagittarius"
	return sign
	
def get_element(sign):
	if sign == "Aries":
		element="FIRE"
	elif sign == "Sagittarius":
		element="FIRE"
	elif sign == "Leo":
		element="FIRE"
	elif sign == "Libra":
		element="AIR"
	elif sign == "Aquarius":
		element="AIR"
	elif sign == "Gemini":
		element="AIR"
	elif sign == "Scorpio":
		element="WATER"
	elif sign == "Cancer":
		element="WATER"
	elif sign == "Pisces":
		element="WATER"
	else:
		element="EARTH"
	return element
	
list = {
	"AIR": "\tAIR signs (thats Gemini, Libra, and Aquarius) are the thinkers, communicators, and doers of the zodiac. They analyze, synthesize, and probe. They breeze through life, never stopping to catch their breath. They have a live and let live mentality, and their intelligence helps them make decisions easily.",	"FIRE": "\tThe FIRE element is one of spontaneity, inspiration, intuition, and big passions. Fiery guys and gals are excitable and impulsive and love to light a fire under others. The fire signs are Aries, Leo, and Sagittarius. ... Fire signs are known to be intuitive and to rely on gut instincts.",
	"WATER": "\tWATER signs—Cancer, Scorpio, and Pisces—are known for being sensitive and sentimental. They tend to hold on to people and items long past their expiration dates, and their emotions are always flowing like the waves of the oceans.",
	"EARTH": "\tEARTH signs (Taurus, Virgo, and Capricorn) are the most grounded peeps on the planet—you know, the ones who always keep it one hundred percent real. They're known to be stable, pragmatic, and unwavering. Slow to anger, it takes a lot of effort to get them frustrated.",
}

print("Is this for 2000s? (Yes/No)")
century=input()
if century == "Yes" or century == "yes":
	print("Then simply subract 1 day")
elif century == "No" or century == "no":
   print(" ")
else:
	print("Invalid Answer")
	
	
born=get_dow(dayofbirth(mm, dd, yy, mc))
born2=get_dow(dayofbirth(mm, dd, yy, mc) - 1)
print(" ")

remainder=yy%4
if remainder == 0 and mm == 1:
	print("You were born on a", born2)
elif remainder == 0 and mm == 2:
	print("You were born on a", born2)
else:
	print("You were born on a", born)

signs=get_sign(mm, dd)
print("You are a(n)", signs)
elements=get_element(get_sign(mm, dd))
print("Your element is", elements)
print(" ")
print(list.get(elements))
