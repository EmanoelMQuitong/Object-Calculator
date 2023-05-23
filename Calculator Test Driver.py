#COLORS 
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'
BORDER = 175*'='

from Calculator import Calculator 
from Calculator2 import Calculator2

print(BOLD+DARKCYAN+BORDER+END)
print(BOLD+DARKCYAN+BORDER+END)
print('\n')

print("CALCULATOR STATUS:")
print('\n')
print(BOLD+GREEN+"Calculator 1 is working fine..."+END)

print(BOLD+GREEN+"Calculator 2 is working fine..."+END) 

print('\n')
print(BOLD+DARKCYAN+BORDER+END)
print(BOLD+DARKCYAN+BORDER+END)

print('\n')

print(BOLD+GREEN+"Calculator 1:"+END)
print('\n')
print("Description:")
print('\n')
print(" This calculator allow you to perform basic operations such as addition, subtraction, multiplication and division.")
print("It allows the user to perform basic operations with a three (3) decimal places.")
print("The progress of any operation used will be written in 'History.txt'.")
print('\n')
print(BOLD+DARKCYAN+BORDER+END)
print(BOLD+DARKCYAN+BORDER+END)


print('\n')

print(BOLD+GREEN+"Calculator 2:"+END)
print('\n')
print("Description:")
print('\n')
print(" This calculator allow you to perform basic operations such as addition, subtraction, multiplication and division.")
print("It allows the user to perform basic operations without any decimal places.")
print("However, there is a special case in this calculator. When division is used, the remainder will be stated.")
print("The progress of any operation used will be written in 'History.txt'.")
print('\n')
print(BOLD+DARKCYAN+BORDER+END)
print(BOLD+DARKCYAN+BORDER+END)

#while loop
Cal1 = Calculator() 
response = input("Would you like to open Calculator 1?('yes' or 'no'): ")
if response == 'yes':
    with open('History.txt', 'a') as History1:
        History1.write('\n')
        History1.write("Calculator 1 History"), History1.write('\n')
    
    while response == 'yes':
        operation = input("Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use?: ")
    
        if operation.lower() == 'addition':
            Cal1.addition()
            print('\n')    
            response = input("Would you like to repeat ADDITION?('yes' or 'no'): ")

            while response == 'yes':
                Cal1.addition()
                print('\n')    
                response = input("Would you like to repeat ADDITION?('yes' or 'no'): ") 

        elif operation.lower() == 'subtraction':
            Cal1.subtraction()
            print('\n')    
            response = input("Would you like to repeat SUBTRACTION?('yes' or 'no'): ")

            while response == 'yes':
                Cal1.subtraction()
                print('\n')    
                response = input("Would you like to repeat SUBTRACTION?('yes' or 'no'): ")
    
        elif operation.lower() == 'multiplication':
            Cal1.multplication()
            print('\n')    
            response = input("Would you like to repeat MULTIPLICATION?('yes' or 'no'): ")

            while response == 'yes':
                Cal1.multplication()
                print('\n')    
                response = input("Would you like to repeat MULTIPLICATION?('yes' or 'no'): ")
        
        elif operation.lower() == 'division':
            Cal1.division()
            print('\n')    
            response = input("Would you like to repeat DIVISION?('yes' or 'no'): ")

            while response == 'yes':
                Cal1.division()
                print('\n')    
                response = input("Would you like to repeat DIVISION?('yes' or 'no'): ")
    
        else:
            raise Exception(RED+"PLEASE CHOOSE FROM THE FOLLOWING CHOICES ONLY.")
        
        print('\n')
        response = input("Would you like to open Calculator 1?('yes' or 'no'): ")

print('\n')
print(BOLD+RED+"Turning off Calculator 1..."+END)
print('\n')
print(BOLD+PURPLE+BORDER+END)
print(BOLD+PURPLE+BORDER+END)



Cal2 = Calculator2() 
response = input("Would you like to open Calculator 2?('yes' or 'no'): ")

if response == 'yes':
    with open('History.txt', 'a') as History2:
        History2.write('\n')
        History2.write("Calculator 2 History"), History2.write('\n')
    
    while response == 'yes':
        operation = input("Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use?: ")
    
        if operation.lower() == 'addition':
            Cal2.addition()
            print('\n')    
            response = input("Would you like to repeat ADDITION?('yes' or 'no'): ")

            while response == 'yes':
                Cal2.addition()
                print('\n')    
                response = input("Would you like to repeat ADDITION?('yes' or 'no'): ") 

        elif operation.lower() == 'subtraction':
            Cal2.subtraction()
            print('\n')    
            response = input("Would you like to repeat SUBTRACTION?('yes' or 'no'): ")

            while response == 'yes':
                Cal2.subtraction()
                print('\n')    
                response = input("Would you like to repeat SUBTRACTION?('yes' or 'no'): ")
    
        elif operation.lower() == 'multiplication':
            Cal2.multplication()
            print('\n')    
            response = input("Would you like to repeat MULTIPLICATION?('yes' or 'no'): ")

            while response == 'yes':
                Cal2.multplication()
                print('\n')    
                response = input("Would you like to repeat MULTIPLICATION?('yes' or 'no'): ")
        
        elif operation.lower() == 'division':
            Cal2.division()
            print('\n')    
            response = input("Would you like to repeat DIVISION?('yes' or 'no'): ")

            while response == 'yes':
                Cal2.division()
                print('\n')    
                response = input("Would you like to repeat DIVISION?('yes' or 'no'): ")
    
        else:
            raise Exception(RED+"PLEASE CHOOSE FROM THE FOLLOWING CHOICES ONLY.")
        
        print('\n')
        response = input("Would you like to continue using Calculator 2?('yes' or 'no'): ")


print('\n')
print(BOLD+RED+"Turning off Calculator 2..."+END)
print('\n')

print(BOLD+BORDER+END)
print(BOLD+BORDER+END)