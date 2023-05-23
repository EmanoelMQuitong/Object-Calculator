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
## Guide
###
# Calculator 2
## Guide

### 
# Guide
