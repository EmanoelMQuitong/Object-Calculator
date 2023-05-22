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

#while loop
Cal1 = Calculator() 
response = input("Would you like to open Calculator 1?('yes' or 'no'): ")
if response == 'yes':
    with open('History.txt', 'a') as History1:
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

print(BOLD+PURPLE+BORDER+END)
print(BOLD+PURPLE+BORDER+END)