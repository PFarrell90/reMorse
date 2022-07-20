from readline import append_history_file
import morse

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

#while loop, length of input, do stuff
i=0
while i < (len(input)):
   currentChar = input[i]
   if (currentChar == " "):
    print("Hey, this is a blank space.")
    ResultArray.append(currentChar)
   elif (currentChar == "."):
    print("Found period. STOP")
    ResultArray.append("STOP") 
   elif (input[i].isalnum()):
    #currentChar = input[i]
    ResultArray.append(currentChar)
   else:
    print(input[i] + " is not alphanumeric. Sorry, guy.")
   #ResultArray.append(input[i])
   #print(input[i],end="")
   i += 1

#print ("Test", ResultArray)
print (ResultArray)

#print("I'm 40% titanium.")