from readline import append_history_file
import morse
from morse import MorseArray

InputArray = []
ResultArray = []

input: str = "The quick BROWN fox JUMPED over the lAzY dOg.@!#!@$%$@"
#print("Original input: " + input)
input = input.lower()
#print ("This is lower case: " + input) #Test .lower method

#main while loop, length of input, do stuff
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

   #else:
    #print(input[i] + " is not alphanumeric. Sorry, guy.")
   #ResultArray.append(input[i])
   #print(input[i],end="")
   i += 1

#print (ResultArray)

tempint = 0
while tempint < len(ResultArray):
    print(ResultArray[tempint],end="")
    tempint += 1 

#print("I'm 40% titanium.")