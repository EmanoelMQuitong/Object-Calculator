#COLORS 
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'
BORDER = 175*'='

from Calculator import Calculator_Override
from Calculator2 import Calculator_Override2




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
Cal1 = Calculator_Override() 
response = input("Would you like to open Calculator 1?('yes' or 'no'): ")
if response == 'yes':
    with open('History.txt', 'a') as History1:
        History1.write('\n')
        History1.write("Calculator 1 History"), History1.write('\n')
    
    while response == 'yes':
        operation = input("Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use?: ")
        
        print('\n')
        print(BOLD+DARKCYAN+BORDER+END)
        print('\n')

        if operation.lower() == 'addition':
            input1 = input("Enter your first number:   ")
            input2 = input("Enter your second number:   ")
            print('\n')
            add = Cal1.addition(input1, input2)
            print(input1, " + ", input2, " = ", add)
            print('\n')

            history = open('History.txt', 'a')
            history.write(input1),history.write(' + '), history.write(input2), history.write(' = '), history.write(add), history.write('\n')
            history.close()
            
            response = input("Would you like to repeat ADDITION?('yes' or 'no'): ")
            

            while response == 'yes':
                print('\n')
                print(BOLD+DARKCYAN+BORDER+END)
                input1 = input("Enter your first number:   ")
                input2 = input("Enter your second number:   ")
                print('\n')
                add = Cal1.addition(input1, input2)
                print(input1, " + ", input2, " = ", add)
                
                print('\n')

                history = open('History.txt', 'a')
                history.write(input1),history.write(' + '), history.write(input2), history.write(' = '), history.write(add), history.write('\n')
                history.close()

                response = input("Would you like to repeat ADDITION?('yes' or 'no'): ") 

        elif operation.lower() == 'subtraction':
            input1 = input("Enter your first number:   ")
            input2 = input("Enter your second number:   ")

            print('\n')

            subtract = Cal1.subtraction(input1, input2)
            print(input1, " - ", input2, " = ", subtract)
            print('\n')

            history = open('History.txt', 'a')
            history.write(input1),history.write(' - '), history.write(input2), history.write(' = '), history.write(subtract), history.write('\n')
            history.close()

            response = input("Would you like to repeat SUBTRACTION?('yes' or 'no'): ")

            while response == 'yes':
                print('\n')
                print(BOLD+DARKCYAN+BORDER+END)

                input1 = input("Enter your first number:   ")
                input2 = input("Enter your second number:   ")
                print('\n')

                subtract = Cal1.subtraction(input1, input2)
                print(input1, " - ", input2, " = ", subtract)
                print('\n')

                history = open('History.txt', 'a')
                history.write(input1),history.write(' - '), history.write(input2), history.write(' = '), history.write(subtract), history.write('\n')
                history.close()

                response = input("Would you like to repeat SUBTRACTION?('yes' or 'no'): ")
    
        elif operation.lower() == 'multiplication':
            input1 = input("Enter your first number:   ")
            input2 = input("Enter your second number:   ")
            product = Cal1.multiplication(input1, input2)
            print(input1, " x ", input2, " = ", product)
            print('\n')

            history = open('History.txt', 'a')
            history.write(input1),history.write(' x '), history.write(input2), history.write(' = '), history.write(product), history.write('\n')
            history.close()

            response = input("Would you like to repeat MULTIPLICATION?('yes' or 'no'): ")

            while response == 'yes':
                print('\n')
                print(BOLD+DARKCYAN+BORDER+END)

                input1 = input("Enter your first number:   ")
                input2 = input("Enter your second number:   ")

                print('\n')

                product = Cal1.multiplication(input1, input2)
                print(input1, " x ", input2, " = ", product)
                print('\n') 

                history = open('History.txt', 'a')
                history.write(input1),history.write(' x '), history.write(input2), history.write(' = '), history.write(product), history.write('\n')
                history.close()

                response = input("Would you like to repeat MULTIPLICATION?('yes' or 'no'): ")
        
        elif operation.lower() == 'division':
            input1 = input("Enter your first number:   ")
            input2 = input("Enter your second number:   ")

            print('\n')

            qoutient = Cal1.division(input1, input2)
            print(input1, " / ", input2, " = ", qoutient)
            print('\n')

            history = open('History.txt', 'a')
            history.write(input1),history.write(' / '), history.write(input2), history.write(' = '), history.write(qoutient), history.write('\n')
            history.close()

            response = input("Would you like to repeat DIVISION?('yes' or 'no'): ")

            while response == 'yes':

                print('\n')
                print(BOLD+DARKCYAN+BORDER+END)

                input1 = input("Enter your first number:   ")
                input2 = input("Enter your second number:   ")

                print('\n')

                qoutient = Cal1.division(input1, input2)
                print(input1, " / ", input2, " = ", qoutient)
                print('\n')

                history = open('History.txt', 'a')
                history.write(input1),history.write(' / '), history.write(input2), history.write(' = '), history.write(qoutient), history.write('\n')
                history.close()

                response = input("Would you like to repeat DIVISION?('yes' or 'no'): ")
    
        else:
            raise Exception(RED+"PLEASE CHOOSE FROM THE FOLLOWING CHOICES ONLY.")
        
        print(BOLD+DARKCYAN+BORDER+END)
        print(BOLD+DARKCYAN+BORDER+END)

        print('\n')
        response = input("Would you like to continue using Calculator 1?('yes' or 'no'): ")

print('\n')
print(BOLD+RED+"Turning off Calculator 1..."+END)
print('\n')
print(BOLD+PURPLE+BORDER+END)
print(BOLD+PURPLE+BORDER+END)



Cal2 = Calculator_Override2() 
response = input("Would you like to open Calculator 2?('yes' or 'no'): ")

if response == 'yes':
    with open('History.txt', 'a') as History2:
        History2.write('\n')
        History2.write("Calculator 2 History"), History2.write('\n')
    
    while response == 'yes':
        operation = input("Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use?: ")
        
        print('\n')
        print(BOLD+DARKCYAN+BORDER+END)
        print('\n')

        if operation.lower() == 'addition':

            input1 = input("Enter your first number:   ")
            input2 = input("Enter your second number:   ")
            print('\n')
            add = Cal2.addition(input1, input2)
            print(input1, " + ", input2, " = ", add)
            print('\n')

            history = open('History.txt', 'a')
            history.write(input1),history.write(' + '), history.write(input2), history.write(' = '), history.write(add), history.write('\n')
            history.close()

            response = input("Would you like to repeat ADDITION?('yes' or 'no'): ")
            

            while response == 'yes':
                print('\n')
                print(BOLD+PURPLE+BORDER+END)

                input1 = input("Enter your first number:   ")
                input2 = input("Enter your second number:   ")

                print('\n')

                add = Cal2.addition(input1, input2)
                print(input1, " + ", input2, " = ", add)
                
                print('\n')

                history = open('History.txt', 'a')
                history.write(input1),history.write(' + '), history.write(input2), history.write(' = '), history.write(add), history.write('\n')
                history.close()

                response = input("Would you like to repeat ADDITION?('yes' or 'no'): ") 

        elif operation.lower() == 'subtraction':
            input1 = input("Enter your first number:   ")
            input2 = input("Enter your second number:   ")

            print('\n')

            subtract = Cal2.subtraction(input1, input2)
            print(input1, " - ", input2, " = ", subtract)
            print('\n')

            history = open('History.txt', 'a')
            history.write(input1),history.write(' - '), history.write(input2), history.write(' = '), history.write(subtract), history.write('\n')
            history.close()
            response = input("Would you like to repeat SUBTRACTION?('yes' or 'no'): ")

            while response == 'yes':
                print('\n')
                print(BOLD+PURPLE+BORDER+END)

                input1 = input("Enter your first number:   ")
                input2 = input("Enter your second number:   ")
                print('\n')

                subtract = Cal2.subtraction(input1, input2)
                print(input1, " - ", input2, " = ", subtract)
                print('\n')

                history = open('History.txt', 'a')
                history.write(input1),history.write(' - '), history.write(input2), history.write(' = '), history.write(subtract), history.write('\n')
                history.close()

                response = input("Would you like to repeat SUBTRACTION?('yes' or 'no'): ")
    
        elif operation.lower() == 'multiplication':
            input1 = input("Enter your first number:   ")
            input2 = input("Enter your second number:   ")
            product = Cal2.multiplication(input1, input2)
            print(input1, " x ", input2, " = ", product)
            print('\n')

            history = open('History.txt', 'a')
            history.write(input1),history.write(' x '), history.write(input2), history.write(' = '), history.write(product), history.write('\n')
            history.close()

            response = input("Would you like to repeat MULTIPLICATION?('yes' or 'no'): ")

            while response == 'yes':
                print('\n')
                print(BOLD+PURPLE+BORDER+END)

                input1 = input("Enter your first number:   ")
                input2 = input("Enter your second number:   ")

                print('\n')

                product = Cal2.multiplication(input1, input2)
                print(input1, " x ", input2, " = ", product)
                print('\n') 

                history = open('History.txt', 'a')
                history.write(input1),history.write(' x '), history.write(input2), history.write(' = '), history.write(product), history.write('\n')
                history.close()

                response = input("Would you like to repeat MULTIPLICATION?('yes' or 'no'): ")
        
        elif operation.lower() == 'division':
            input1 = input("Enter your first number:   ")
            input2 = input("Enter your second number:   ")

            print('\n')

            qoutient = Cal2.division(input1, input2)
            remainder = Cal2.div_rem(input1, input2)
            print(input1, " / ", input2, " = ", qoutient, " Remainder ", remainder)
            print('\n')

            history = open('History.txt', 'a')
            history.write(input1),history.write(' / '), history.write(input2), history.write(' = '), history.write(qoutient), history.write(" Remainder "),history.write(remainder),  history.write('\n')
            history.close()

            response = input("Would you like to repeat DIVISION?('yes' or 'no'): ")

            while response == 'yes':

                print('\n')
                print(BOLD+PURPLE+BORDER+END)

                input1 = input("Enter your first number:   ")
                input2 = input("Enter your second number:   ")

                print('\n')

                qoutient = Cal2.division(input1, input2)
                remainder = Cal2.div_rem(input1, input2)
                print(input1, " / ", input2, " = ", qoutient, " Remainder ", remainder)
                print('\n')

                history = open('History.txt', 'a')
                history.write(input1),history.write(' / '), history.write(input2), history.write(' = '), history.write(qoutient), history.write(" Remainder "),history.write(remainder),  history.write('\n')
                history.close()

                response = input("Would you like to repeat DIVISION?('yes' or 'no'): ")
    
        else:
            raise Exception(RED+"PLEASE CHOOSE FROM THE FOLLOWING CHOICES ONLY.")
        
        print(BOLD+PURPLE+BORDER+END)
        print(BOLD+PURPLE+BORDER+END)

        print('\n')
        response = input("Would you like to continue using Calculator 2?('yes' or 'no'): ")


print('\n')
print(BOLD+RED+"Turning off Calculator 2..."+END)
print('\n')

print(BOLD+BORDER+END)
print(BOLD+BORDER+END)