# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 22:59:02 2014

@author: twoism
"""
from random import randint

done = False
miles_traveled = 0
thirst = 0
camel_fatigue = 0
natives_distance = -20
drinks_in_canteen = 5

print "Welcome to Camel!"
print "You have stolen a camel to make your way across the great Gobi desert!"
print "The natives want their camel back and are chasing you down! Survive your"
print "desert trek and outrun the natives."

while not done:

	if miles_traveled >= 200:
		print "\nYou've escaped from the natives!\n"
		done = True

	elif randint(1,100) > 95:
		drinks_in_canteen = 5
		thirst = 0
		camel_fatigue = 0
		print "\nYou have found an oasis! Be sure to fill your canteen!\n"
		print "\nA. Drink from your canteen."
		print "B. Ahead moderate speed."
		print "C. Ahead full speed."
		print "D. Stop for the night."
		print "E. Status check."
		print "Q. Quit."
		user_choice = str(raw_input("\nMake a selection:")).upper()
		
	else:
		print "\nA. Drink from your canteen."
		print "B. Ahead moderate speed."
		print "C. Ahead full speed."
		print "D. Stop for the night."
		print "E. Status check."
		print "Q. Quit."
		user_choice = str(raw_input("\nMake a selection:")).upper()
	    
	if natives_distance >= miles_traveled:
		print "\nYou have been caught by the natives!\n"
		done = True

	elif (miles_traveled - abs(natives_distance)) <= 15:
		print "The natives are getting close!"
    
	if thirst == 4:
		print "You are thirsty."
	elif thirst == 5:
		print "You are VERY thirsty!"
	elif thirst >= 6:
		print "\nYou have died of thrist.\n"
		break
    
	if len(user_choice) != 1:
		print "\nPlease make a valid selection."
	
	elif user_choice == "Q":
		done = True
		
	elif user_choice == "E":
		print "\nMiles traveled:", miles_traveled
		print "Drinks in canteen:", drinks_in_canteen
		print "The natives are %s miles behind you." % abs(miles_traveled - abs(natives_distance))
		
	elif user_choice == "D":
		camel_fatigue = 0
		natives_distance += randint(4, 10)
		print "The camel is happy and rested."
		
	elif user_choice == "C":
		miles_traveled += randint(10, 20)
		camel_fatigue += randint(1,3)
		natives_distance += randint(7, 14)
		thirst += 1
		
	elif user_choice == "B":
		miles_traveled += randint(5,12)
		camel_fatigue += 1
		natives_distance += randint(7,14)
		thirst += 1
		
	elif user_choice == "A":
		if drinks_in_canteen <= 0:
			print "There are no drinks left in the canteen."
			
		elif drinks_in_canteen >= 1:
			drinks_in_canteen -= 1
			thirst = 0
			
	else:
		print "\nPlease make a valid selection"

print "Thank you for playing!"