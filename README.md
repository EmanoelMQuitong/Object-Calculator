# Object-Calculator
  This program consists of 2 objects which is Calculator 1 and Calculator 2, it is followed by a Calculator Test Driver which uses the two different Calculator at once. The progress while using the calculators will be transferred immediately at 'History.txt'.

###

# Calculator Test Driver
  This program calls the objects that'll be used for performing basic operations such as addition, multiplication and division. 
  ## Flow
  1. The Calculator status will be presented.
  2. The user will be asked to asked if it wanted to use Calculator 1.
      + If yes, then the user will proceed using Calculator 1. 'Histor.txt' will be updated that the user used Calculator 1. 
     ```
     'History.txt' will print 
     Calculator 1 History.
     ```
         If not, then it will proceed using Calculator 2.
     
     + Next, the user will be asked which operation will be used.Addition, Subtraction, Multiplication and Division are the only choices. 
     ```
     Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use?: 
     ```
     + It will create a while loop that will repeat the operation. It can only be stopped responding 'no' when asked.
     ```
     while response == 'yes':
         Cal1.addition()
         response = input("Would you like to repeat ADDITION?('yes' or 'no'): ") 
     ```
     + When the while loop is broken, the it will repeat the process for another operation.
     + If using calculator 1 is done, it will turn off and proceed Calculator 2.
     ```
      "Turning off Calculator 1..."
     ```
     
   3. The user will be asked to asked if it wanted to use Calculator 2.
      + If yes, then the user will proceed using Calculator 2. 'Histor.txt' will be updated that the user used Calculator 2. 
      ```
      'History.txt' will print 
      Calculator 2 History.
      ```
     
         If not, Calculator 2 will turn off.
       + Next, the user will be asked which operation will be used.Addition, Subtraction, Multiplication and Division are the only choices.
        
        ```
        Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use?: 
        ```
       + It will create a while loop that will repeat the operation. It can only be stopped responding 'no' when asked.
       ```
        while response == 'yes':
            Cal2.addition()
            response = input("Would you like to repeat ADDITION?('yes' or 'no'): ") 
        ```
     
        + When the while loop is broken, the it will repeat the process for another operation.
        + If using calculator 2 is done, it will turn off. 
      ```
        "Turning off Calculator 2..."
      ```
   

###

# Calculator 1
  This calculator allow you to perform basic operations such as addition, subtraction, multiplication and division.It allows the user to perform basic operations with a three (3) decimal places. The progress of any operation used will be written in 'History.txt'.

## Guide

Create an 2 input that'll be involved in operations. Then use it for the operation. Make sure that the float() is applied in inputs for the process. Lastly, associate the result with "%.3f" just like on the given below:
```
def addition(calc):
  calc.input1 = input("Enter first number: ")
  calc.input2 = input("Enter second number: ")
  result = float(calc.input1) + float(calc.input2)
  
  calc.result1 = "%.3f"%result
```
This process is applied to all operation. However, The operand is changed per operation.

###
# Calculator 2
  This calculator allow you to perform basic operations such as addition, subtraction, multiplication and division. It allows the user to perform basic operations without any decimal places. However, there is a special case in this calculator. When division is used, the remainder will be stated.The progress of any operation used will be written in 'History.txt'.
 
 
## Guide
Just like the first calculator create an 2 input that'll be involved in operations. Then use it for the operation.  Use int() function on the inputs like on the given below:
```
def addition(calc):
  calc.input1 = input("Enter first number: ")
  calc.input2 = input("Enter second number: ")
  result = int(calc.input1) + int(calc.input2)
    
```
This process is applied to all operation. However, The operand is changed per operation.

There is a special case  division where in remainder is involved. Modulus (%) whould be applied from first input followed by second input.

```
def division(calc):
  calc.input1 = input("Enter first number: ")
  calc.input2 = input("Enter second number: ")
  result = int(calc.input1) / int(calc.input2)
  remainder = int(calc.input1) % int(calc.input2)
    
```

### 

