#!/usr/bin/env python3

ron = "lemme Smash"
print (ron)
print ("The fifth letter in the string above is: " + ron[4] + "\n")

print (ron.upper())
print (ron.lower())

pi = 3.14
print ("Use str() to print a number with a string like this " + str(pi))
print ( "'"+ ron + "' contains " + str(len(ron)) + " characters.")

print ("\nBetter than concatenating:")
print ("Becky %s%s" % (ron, ", Plz!")) 
