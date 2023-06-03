#Colors and text forms
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'
BORDER = 175*'='
print(BOLD+PURPLE+BORDER+END)

#Class Calculator Default

class Calculator:
    def __init__(calc, input1 = 0,input2 = 0, result1 = 0):
        calc.input1 = input1
        calc.input2 = input2
        calc.result1 = result1

#Addition function: While loop function, File history
    def addition(calc):
        try:
            print(BOLD+PURPLE+BORDER+END)
            print('\n')
            print(BOLD+BLUE+"Enter your first number:"+END)
            calc.input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            calc.input2 = input(" ")
            result = float(calc.input1) + float(calc.input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )

        calc.result1 = "%.3f"%result
        print('\n')
        print(str(calc.input1) ,"+", str(calc.input2),"=", calc.result1)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' + '), history.write(calc.input2), history.write(' = '), history.write(calc.result1), history.write('\n')
        
        print('\n')
        print(BOLD+PURPLE+BORDER+END)

#Subtraction function: WHile loop function
    def subtraction(calc):
        try:
            print(BOLD+PURPLE+BORDER+END)
            print('\n')

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
    
        calc.result1 = "%.3f"%result
        print('\n')
        print(str(calc.input1) ,"-", str(calc.input2),"=", calc.result1)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' - '), history.write(calc.input2), history.write(' = '), history.write(calc.result1), history.write('\n')

        print('\n')
        print(BOLD+PURPLE+BORDER+END)
            
#Multiplication function: While loop function
    def multplication(calc):
        try:
            print(BOLD+PURPLE+BORDER+END)
            print('\n')

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

        calc.result1 = "%.3f"%result
        print('\n')
        print(str(calc.input1) ,"x", str(calc.input2),"=", calc.result1)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' x '), history.write(calc.input2), history.write(' = '), history.write(calc.result1), history.write('\n')

        print('\n')
        print(BOLD+PURPLE+BORDER+END)

#Division function: While loop function
    def division(calc):
        try:
            print(BOLD+PURPLE+BORDER+END)
            print('\n')

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

        calc.result1 = "%.3f"%result
        print('\n')
        print(str(calc.input1) ,"/", str(calc.input2),"=", calc.result1)
        history = open('History.txt', 'a')
        history.write(calc.input1),history.write(' / '), history.write(calc.input2), history.write(' = '), history.write(calc.result1), history.write('\n')

        print('\n')
        print(BOLD+PURPLE+BORDER+END)

class Calculator_Override(Calculator):
    def __init__(calc, input1 = 0,input2 = 0, result1 = 0):
        calc.input1 = input1
        calc.input2 = input2
        calc.result1 = result1

    def addition(calc, input1, input2):
        result = float(input1) + float(input2)
        result = "%.3f"%result
        return result

    def subtraction(calc, input1, input2):
        result = float(input1) - float(input2)
        result = "%.3f"%result
        return result

    def multiplication(calc, input1, input2):
        result = float(input1) * float(input2)
        result = "%.3f"%result
        return result

    def division(calc, input1, input2):
        result = float(input1) / float(input2)
        result = "%.3f"%result
        return result  