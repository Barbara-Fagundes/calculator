# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:54:30 2017

@author: Barbara F.
"""

#The program asks the user to enter a separate numeric operator and two numeric values.  Depending upon the operator, the corresponding arithmetic operation is performed. The program lets you know if you entered an invalid operator, that is one other than +, -, %, , /, //, * 

#Declaration and assignment from variables  
isNoInt = True
wantMore = True
ope = ""
wish = ""
num1 = 0
num2 = 1
res = 0

#definition from the function doTheMath which performs and prints in console the result from basic mathematical operations, with an opetator and two integers given in arguments.
def doTheMath (sign, int1, int2):
    if (sign == "+"):
        res = (int1 + int2)
        print (str(int1) + "+" + str(int2) + " = " + str(res) + "\n")
    elif (sign == "-"):
        res = (int1 - int2)
        print (str(int1) + "-" + str(int2) + " = " + str(res) + "\n")
    elif (sign == "%"):
        res = (int1%int2)
        print (str(int1) + "mod" + str(int2) + " = " + str(res) + "\n")
    elif (sign == "*"):
        res = (int1 * int2)
        print (str(int1) + "*" + str(int2) + " = " + str(res) + "\n")
    elif (sign == "/"):
        res = (int1 / int2)
        res = (float(int(res * 100)))/100 #rounded at 2 decimals
        print (str(int1) + "/" + str(int2) + " = " + str(res) + " (Precision is at 2 decimals!)\n")
    elif (sign == "//"):
        res = (int1//int2)
        print (str(int1) + "//" + str(int2) + " = " + str(res) + "\n")
    elif (sign == "**"):
        res = (int1**int2)
        print (str(int1) + "^" + str(int2) + " = " + str(res) + "\n")
            
#displays a hello message
print ("Hello, I am a mathematical calculator!")

#Loops if you wish to continue
while (wantMore): #while you choose to make more mathematics 

#Input from the variables 

#first number
    isNoInt = True #set to True again so that we can start next loop
    while (isNoInt): #while input is not an integer
        try: #try except block to make sure that input is an integer number
            num1 = int(input ("Input an integer:\n")) #Trying to cast input into an integer
            isNoInt = False #if cast worked means that input is an integer, isNoInt is set to False 
        except ValueError: #if input was no integer number, an error message is displayed
            print ("Wrong input, you are required to ") #back to the top of the loop
        
#the operator
    ope = "" #eventual last operator value is removed from variable
    while (ope != "+" and ope != "-" and ope != "%" and ope != "*" and ope != "/" and ope != "//" and ope != "**"): #for as long as input is not one from the allowed variables 
        ope = input("Input an operator corresponding to the mathematical operation that you want to perform (+,-,%,*,/,//,**):\n") #displays a message requesting for a string input that will decide what operation will be calculated

#second number 
    isNoInt = True #set to True again so that we can start next loop
    while (isNoInt): #while input is not an integer   
        try: #try except block to make sure that input is an integer number
            num2 = int(input ("Input another integer that's not a 0 whether the choosen operation was a division:\n")) #Trying to cast input into an integer
            if (num2 == 0 and (ope == "%" or ope == "/" or ope == "//")): #if the operation is a division and the input a 0
                print ("You can't divide by 0") #an error message is printed 
            else:
                isNoInt = False #if cast worked and divider is not 0, isNoInt is set to False 
        except ValueError: #if input was no integer number, an error message is displayed
            print ("Wrong input, you are required to") #back to the top of the loop
            
#Let's do some mathematical calcul
    doTheMath(ope, num1, num2)
    
#Do more?
    wish = "" #set back to None so that we enter loop at first 
    while (wish != "Y" and wish != "N"): #while input is not Y or N
        wish = input ("Do you wish to do more mathematics (Y/N)?\n") #message is displayed to ask for input
    if (wish == "N"): #If user doesn't want to go further
        wantMore = False #Flag from first loop is removed 
        
#displays a goodbye message when user is done 
print ("Goodbye, see you next time!")
