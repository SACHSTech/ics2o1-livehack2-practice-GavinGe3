"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Determines if a triangle is right-angled using the inputted sidelengths of the triangle
 
Author: Ge.G
 
Created:  12/02/2021
------------------------------------------------------------------------------
"""
print("******Right-angled triangle determiner")

# get triangle side-lengh info
sideOne = float(input("Enter the length of side 1: "))
sideTwo = float(input("Enter the length of side 2: "))
sideThree = float(input("Enter the length of side 3: "))

# compute squares of sides
sideOneSquared = sideOne**2
sideTwoSquared = sideTwo**2
sideThreeSquared = sideThree**2

# determine  and output if the triangle is a right-angled triangle
if (sideOneSquared+sideTwoSquared == sideThreeSquared) or (sideTwoSquared+sideThreeSquared == sideOneSquared) or (sideThreeSquared+sideOneSquared == sideTwoSquared):
  print(f"\nThe triangle with side lengths {sideOne}, {sideTwo}, and {sideThree} form a right-angled triangle.")
else:
  print(f"\nThe triangle with side lengths {sideOne}, {sideTwo}, and {sideThree} do not form a right-angled triangle.")
