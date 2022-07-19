import numpy
import morse_oneline

#1. Get input [string] via a text box in a webpage \\This is hopefully handled by the frontend page
#2. Store as var, convert all characters in input .toLowerCase
    #a. strip anything that is a non alpha-numeric character 
#3. for each character in [string]<input>, loop through array "morse" 
#4. Store value per each character to array "Result"
#5. Pipe result var via Lambda to SNS/SES (text or email)

input2 = "Morse code, for all your programming needs. "
InputArray = []
ResultArray = []

input: str = "I DON'T KNOW WHAT WE'RE YELLING ABOUT. LOUD NOISES."
lowerCase = input.lower()
print ("This is lower case:" + lowerCase) #Test .lower method

print(lowerCase[2])


#This is far easier: 
x: int = 0
print(x)
x += 2
print(x) #This also seems to work just fine, so why is it complaining that the string index isn't an int???
# Is this because append's method is structured to pass through a string? 

#for x in input:
#    if x == mor
#    ResultArray.append(int input[x]) #This right here is causing a problem. "string indices must be integers"
#    x += 1


#while loop, length of input, do stuff
i=0
while i < (len(input)):
   ResultArray.append(input[i])
   print(input[i],end="")
   i += 1

#print ("This is the result:" + ResultArray)

print("I'm 40% titanium.")