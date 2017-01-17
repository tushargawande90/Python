
# coding: utf-8

# # Python Assignment 1 

# ### Part 1 : Number Guessing Game

# In[1]:

import random
#Selecting a random number using randint function under random package
selectedNumber= random.randint(1,20)

flag=False;
print("Number Guessing Game Starts...")
for i in range(5) :
    inputNumber=int(input('Enter your guess number in range[1 to 20] :'))
    if (inputNumber == selectedNumber):
        print("You guessed it right!")
        flag=True
        break
    else :
        if(inputNumber > (selectedNumber+2)):
            print("Your guess is too high")
        elif(inputNumber < (selectedNumber-2)):
            print("Your guess is too low")
        else:
            print("You are close :)")

if(flag==True):
    print("You won the game!")
else:
    print("You lost the game, better luck next time.")


# ### Part 2 : ROT 13 Cypher

# In[2]:

#Defining a function to do the ROT13 cypher. It accepts input string and an optional 'case' argument.
#By default the value of this argument is kept as Upper.

def cypherROT13(inputString, case="Upper"):
    cypher = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                               "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    if(case=="Lower"):
        return inputString.lower().translate(cypher)
    if(case=="Upper"):
        return inputString.upper().translate(cypher)
    return "Please input case as 'Upper' or 'Lower'"

# Testing the cypher function
# 1. "Test" Just a random text
print(cypherROT13(cypherROT13(input("Test Case 1: "))))
# 2. "002Test002" Input as combination of numbers and characters
print(cypherROT13(cypherROT13(input("Test Case 2: "),"Lower"),"Lower"))
# 3. "Testing  Space Testing"
print(cypherROT13(cypherROT13(input("Test Case 3: "),"Upper"),"Upper"))
# 4. "0123456789"
print(cypherROT13(cypherROT13(input("Test Case 4: "))))
# 5. "all lower cases"
print(cypherROT13(cypherROT13(input("Test Case 5: "),"Lower"),"Lower"))
# 6. "ALL UPPER CASES"
print(cypherROT13(cypherROT13(input("Test Case 6: "),"Upper"),"Upper"))

