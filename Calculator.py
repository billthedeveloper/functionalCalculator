#This program is a functional calculator that a user can use to
#do calculations on any two numbers they choose

#A statement that allows the user to call a function stored in the math module.
#For example the squareroot function that is going to be used later on in this
#program
import math
#Constants for menu choices
Addition = 1
Subtraction = 2
Multiplication = 3
Division = 4
Squareroot = 5
Exit=6
# creates a function called main that will be used to call other functions
#in the program
def main():
  
#Get the two numbers that a user needs to do calculations on and store
#them in two variables.
#In these two statements the input is converted from a string
#to a numerical string by the int function
#so that the program can do mathematical calculations
    num1= int(input('Enter the first number: '))
    num2= int(input('Enter the second number: '))

    #get the users menu choice by calling a function that gets the choice
    #and assigns it to the variable choice
    choice = get_menu_choice()

    #Process the choice based on the menu option they chose             
    if choice == Addition:
            addition(num1, num2)    
    elif choice == Subtraction:
            subtraction(num1, num2)    
    elif choice == Multiplication:
            multiplication(num1, num2) 
    elif choice == Division:
            division(num1, num2)
    elif choice == Squareroot:          
            squareroot(num1, num2)
    elif choice ==Exit:
            print('Exiting')
                   
    #Calls a function that asks the user if they want another calculation
    anotherCalc()

    
# The get_menu_choice function displays the calculator menu that shows the users'
#the different operators they can choose to perform on the numbers
#and gets a validated choice from the user.

def get_menu_choice():
    print("Welcome to the calculator program")
    print("Your options are:")
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Squareroot")
    print("6. Exit")
    print()

    #Get the user's choice.
    choice = int(input("Enter your choice: "))
    #A while loop that validates the user's input and prompts the user to
    #renter his or her choice if its not acceptable
    while choice < Addition or choice > Exit:
        choice = int(input('Enter a valid choice: '))
        
    #return the users choice
    return choice

#creates a function named addition that adds two numbers together
def addition(a, b):
    
    #A statement that adds the two numbers together and assigns the result
    #to the result variable
    result= a + b
    
    #Display the result
    print(result)
    
#creates a function named subtraction that subtracts one number from another
def subtraction(a, b):
    result= a - b

    #Display the result
    print(result)
       
#creates a function named multiplication that multiplies one number from another   
def multiplication(a, b):
    result = a * b
    print(result)

     
#creates a function named division that divides one number from another
def division(a, b):
    result = a / b
    print(result)
    
#creates a function named squareroot that gets the square root of two numbers
def squareroot(a, b):
    square_rt1= math.sqrt(a)
    square_rt2= math.sqrt(b)
    print('The Square root of' ,a, 'is', square_rt1)
    print('The Square root of' ,b, 'is', square_rt2)

#The function that allows this program to be used over and over again for calculations
#If the user desires
def anotherCalc():
    #Asks the user if they want another calculation
    another= input('Calculate again? (Y/N): ')
    
    #Adds the upper method to a condition that is tested, to make case insensitive string comparisions
    #Meaning a lowercase y or upper case Y is acceptable as Yes
    if another.upper()== 'Y': #A conditional statement that executes the block of statements inside it up to the elif clause and ignores the rest of the structure
        main()                #if the condition is true.
                   
    # The program jumps to this clause only when the condition tested in the if statement is false and executes the block of statements in this clause if the second condition is true.
    #If thats the case then the rest of the structure is then ignored. However, if it is false the program jumps to the next elif clause and continues till it finds a condition that is true or no more elif clauses are left. 
    elif another.upper()== 'N':
        print('Goodbye')
    #When the program reaches this part it is because the previous conditions were not true or it ran out of conditions to test.
    else:
        print('ERROR: Enter Y for YES or N for NO.')
        anotherCalc()
main()
