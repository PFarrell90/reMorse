from readline import append_history_file
#import numpy
import morse
from morse import MorseArray


#1. Get input [string] via a text box in a webpage \\This is hopefully handled by the frontend page
#2. Store as var, convert all characters in input .toLowerCase
    #a. strip anything that is a non alpha-numeric character 
#3. for each character in [string]<input>, loop through array "morse" 
#4. Store value per each character to array "Result"
#5. Pipe result var via Lambda to SNS/SES (text or email)

InputArray = []
ResultArray = []

input: str = "The quick BROWN fox JUMPED over the lAzY dOg.@!#!@$%$@"
print("Original input: " + input)
input = input.lower()
print ("This is lower case: " + input) #Test .lower method

###

#while loop, length of input, do stuff
i=0
while i < (len(input)):
   currentChar = input[i]

   if (currentChar == " "):
    print("Hey, this is a blank space.")
    #ResultArray.append(currentChar)
    ResultArray.append("  ")

   elif (currentChar == "."):
    print("Found period. STOP")
    ResultArray.append("STOP") 

   elif (currentChar.isalnum()):
    #currentChar = input[i]
    #Take from the more array the letter or number
    #But we can't pipe "currentChar" because that's an alphanumeric char (or single string)
    #So we need to search through Morse Array's objects until we find it's .Name, then append on hit
    tempint = 0
    while tempint < len(MorseArray):
        if (MorseArray[tempint].Name == currentChar):
            print("Hey, found a match in morse array for: " + currentChar)
            ResultArray.append(MorseArray[tempint].MorseValue)
            ResultArray.append(" ")
        #else:
        #    print("No match found.")
        tempint += 1
    #ResultArray.append(MorseArray[currentChar].MorseValue)

   else:
    print(input[i] + " is not alphanumeric. Sorry, guy.")
   #ResultArray.append(input[i])
   #print(input[i],end="")
   i += 1

#print (ResultArray)

tempint = 0
while tempint < len(ResultArray):
    print(ResultArray[tempint],end="")
    tempint += 1 

#print("I'm 40% titanium.")