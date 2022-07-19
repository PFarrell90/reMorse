#Make an array of all the characters to cipher through

#Discovery 1: Python doesn't have native arrays, it has "lists" 
#So we need to import the "NumPy" module

import numpy
import morse


#import csv
#import morse.csv

#array = np.array([1,2,3,4,5,"This is a string","false"])

#1. Get input [string] via a text box in a webpage
#2. Store as var, convert all characters in input .toLowerCase (or just the entire thing at once)
#3. for each character in [string]<input>, loop through array "morse" 
#4. Store value per each character to array "Result"
#5. Pipe result var via Lambda to SNS/SES (text or email)

#Character class
class Char():
    def __init__(self):
        self.Name = None
        self.MorseValue = None

TestArray = []

TestArray.append(Test1)
TestArray.append(Test2)

#Print the entire array
print (TestArray)

#Print index 0's Name and MorseValue
print ((TestArray[0].Name),(TestArray[0].MorseValue))
print ((TestArray[1].Name),(TestArray[1].MorseValue))



#Vars
#input = <GetInputFromTextBox>

#for each (char in input){

#}

#Should this array become a list of objects with a "MorseValue"?
#So, this would be:

#morseArray = np.array([
#    [A,]
#    ])


#print(array)

print("I'm 40% titanium.")
