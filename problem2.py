"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  Determines if I will go to Europe, California, or stay home based on inputted grades and amount of money earned before the summer
 
Author: Ge.G
 
Created:  12/02/2021
------------------------------------------------------------------------------
"""
print("******Where will I go?******")

# get mark and earnings info
mark = float(input("Enter your mark: "))
earnings = float(input("Enter the amount you earned before the summer: "))

# determine and output where I can go
if mark >= 80 and earnings >= 500:
  print("You can go to Europe")
elif mark >= 80:
  print("You can go to California")
else:
  print("You stay home")
