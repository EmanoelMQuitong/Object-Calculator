#Colors and text forms
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'
BORDER = 175*'='

print(BOLD+BORDER+END)

#Class Calculator Default

class Calculator2:
    def __init__(calc, input1 = 0,input2 = 0, result2 = 0):
        calc.input1 = input1
        calc.input2 = input2
        calc.result2 = result2

#Addition function: While loop function, File history
    def addition(calc):
        try:
            print(BOLD+BORDER+END)
            print('\n')
            print(BOLD+BLUE+"Enter your first number:"+END)
            calc.input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            calc.input2 = input(" ")
            calc.result2 = int(calc.input1) + int(calc.input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and ints are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-int are cannot be used."+ END )

        calc.result2 = str(int(calc.result2))
        print('\n')
        print(str(calc.input1) ,"+", str(calc.input2),"=", calc.result2)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' + '), history.write(calc.input2), history.write(' = '), history.write(calc.result2), history.write('\n')
        
        print('\n')
        print(BOLD+BORDER+END)

#Subtraction function: WHile loop function
    def subtraction(calc):
        try:
            print(BOLD+BORDER+END)
            print('\n')

            print(BOLD+BLUE+"Enter your first number:"+END)
            calc.input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            calc.input2 = input(" ")
            calc.result2 = int(calc.input1) - int(calc.input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and ints are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-int are cannot be used."+ END )
    
        calc.result2 = str(int(calc.result2))
        print('\n')
        print(str(calc.input1) ,"-", str(calc.input2),"=", calc.result2)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' - '), history.write(calc.input2), history.write(' = '), history.write(calc.result2), history.write('\n')

        print('\n')
        print(BOLD+BORDER+END)
            
#Multiplication function: While loop function
    def multplication(calc):
        try:
            print(BOLD+BORDER+END)
            print('\n')

            print(BOLD+BLUE+"Enter your first number:"+END)
            calc.input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            calc.input2 = input(" ")
            calc.result2 = int(calc.input1) * int(calc.input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and ints are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-int are cannot be used."+ END )

        calc.result2 = str(int(calc.result2))
        print('\n')
        print(str(calc.input1) ,"x", str(calc.input2),"=", calc.result2)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' x '), history.write(calc.input2), history.write(' = '), history.write(calc.result2), history.write('\n')

        print('\n')
        print(BOLD+BORDER+END)

#Division function: While loop function
    def division(calc):
        try:
            print(BOLD+BORDER+END)
            print('\n')

            print(BOLD+BLUE+"Enter your first number:"+END)
            calc.input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            calc.input2 = input(" ")
            calc.result2 = int(calc.input1) / int(calc.input2)
            remainder = int(calc.input1) % int(calc.input2)
            
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and ints are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-int are cannot be used."+ END )

        calc.result2 = str(int(calc.result2))
        print('\n')
        print(str(calc.input1) ,"/", str(calc.input2),"=", calc.result2, "Remainder", remainder)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' / '), history.write(calc.input2), history.write(' = '), history.write(calc.result2), history.write(" Remainder "),history.write(remainder),  history.write('\n')

        print('\n')
        print(BOLD+BORDER+END)


class Calculator_Override2(Calculator2):
    def __init__(calc, input1 = 0,input2 = 0, result1 = 0):
        calc.input1 = input1
        calc.input2 = input2
        calc.result1 = result1

    def addition(calc, input1, input2):
        result = int(input1) + int(input2)
        result = "%.0f"%result
        return result

    def subtraction(calc, input1, input2):
        result = int(input1) - int(input2)
        result = "%.0f"%result
        return result

    def multiplication(calc, input1, input2):
        result = int(input1) * int(input2)
        result = "%.0f"%result
        return result

    def division(calc, input1, input2):
        result = int(input1) / int(input2)
        result = "%.0f"%result
        return result
    
    def div_rem(calc, input1, input2):
        result = int(input1) % int(input2)
        remainder = "%.0f"%result
        return remainder
        