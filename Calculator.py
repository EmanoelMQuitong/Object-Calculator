#Colors and text forms
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

#Class Calculator Default

class Calculator:
    def __init__(calc, input1 = 0,input2 = 0):
        calc.input1 = input1
        calc.input2 = input2

#Addition function: While loop function, File history
    def addition(calc):
        try:
            print(BOLD+BLUE+"Enter your first number:"+END)
            calc.calc.input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            calc.input2 = input(" ")
            result = float(calc.input1) + float(calc.input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )

        result = "%.3f"%result
        print('\n')
        print(str(calc.input1) ,"+", str(calc.input2),"=", result)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' + '), history.write(calc.calc.input2), history.write(' = '), history.write(result), history.write('\n')


#Subtraction function: WHile loop function
    def subtraction(calc):
        try:
            print(BOLD+BLUE+"Enter your first number:"+END)
            calc.input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            calc.input2 = input(" ")
            result = float(calc.input1) - float(calc.input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )
    
        result = "%.3f"%result
        print('\n')
        print(str(calc.input1) ,"-", str(calc.input2),"=", result)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' - '), history.write(calc.input2), history.write(' = '), history.write(result), history.write('\n')

#Multiplication function: While loop function
    def multplication(calc):
        try:
            print(BOLD+BLUE+"Enter your first number:"+END)
            calc.input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            calc.input2 = input(" ")
            result = float(calc.input1) * float(calc.input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )

        result = "%.3f"%result
        print('\n')
        print(str(calc.input1) ,"x", str(calc.input2),"=", result)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' x '), history.write(calc.input2), history.write(' = '), history.write(result), history.write('\n')

#Division function: While loop function
    def division(calc):
        try:
            print(BOLD+BLUE+"Enter your first number:"+END)
            calc.input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            calc.input2 = input(" ")
            result = float(calc.input1) / float(calc.input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )

        result = "%.3f"%result
        print('\n')
        print(str(calc.input1) ,"/", str(calc.input2),"=", result)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' / '), history.write(calc.input2), history.write(' = '), history.write(result), history.write('\n')

Cal1 = Calculator()
Cal1.addition()
Cal1.subtraction()
Cal1.multplication()
Cal1.division()
        