//Refactored Python to JS (hopefully?)

//Object constructor
function Char(name,morsevalue) {

        this.Name = name;
        this.MorseValue = morsevalue;
}
var MorseArray = []

//JS Object Contstructions
var Index00 = new Char("a",".-");   
var Index01 = new Char("b","-..."); 
var Index02 = new Char("c","-.-."); 
var Index03 = new Char("d","-..");  
var Index04 = new Char("e",".");    
var Index05 = new Char("f","..-."); 
var Index06 = new Char("g","--.");  
var Index07 = new Char("h","...."); 
var Index08 = new Char("i","..");   
var Index09 = new Char("j",".---"); 
var Index10 = new Char("k","-.-");  
var Index11 = new Char("l",".-.."); 
var Index12 = new Char("m","--");   
var Index13 = new Char("n","-.");   
var Index14 = new Char("o","---");  
var Index15 = new Char("p",".--."); 
var Index16 = new Char("q","--.-"); 
var Index17 = new Char("r",".-.");  
var Index18 = new Char("s","...");  
var Index19 = new Char("t","-");    
var Index20 = new Char("u","..-");  
var Index21 = new Char("v","...-"); 
var Index22 = new Char("w",".--");  
var Index23 = new Char("x","-..-"); 
var Index24 = new Char("y","-.--"); 
var Index25 = new Char("z","--.."); 
var Index26 = new Char("0","----"); 
var Index27 = new Char("1",".---"); 
var Index28 = new Char("2","..--"); 
var Index29 = new Char("3","...-"); 
var Index30 = new Char("4","...."); 
var Index31 = new Char("5","...."); 
var Index32 = new Char("6","-..."); 
var Index33 = new Char("7","--.."); 
var Index34 = new Char("8","---."); 
var Index35 = new Char("9","----"); 

//Push all 36 objects into the MorseArray as a cipher

//js range
//Push all 36 alphanumeric objects to the MorseArray 
MorseArray.push(Index00)
MorseArray.push(Index01)
MorseArray.push(Index02)
MorseArray.push(Index03)
MorseArray.push(Index04)
MorseArray.push(Index05)
MorseArray.push(Index06)
MorseArray.push(Index07)
MorseArray.push(Index08)
MorseArray.push(Index09)
MorseArray.push(Index10)
MorseArray.push(Index11)
MorseArray.push(Index12)
MorseArray.push(Index13)
MorseArray.push(Index14)
MorseArray.push(Index15)
MorseArray.push(Index16)
MorseArray.push(Index17)
MorseArray.push(Index18)
MorseArray.push(Index19)
MorseArray.push(Index20)
MorseArray.push(Index21)
MorseArray.push(Index22)
MorseArray.push(Index23)
MorseArray.push(Index24)
MorseArray.push(Index25)
MorseArray.push(Index26)
MorseArray.push(Index27)
MorseArray.push(Index28)
MorseArray.push(Index29)
MorseArray.push(Index30)
MorseArray.push(Index31)
MorseArray.push(Index32)
MorseArray.push(Index33)
MorseArray.push(Index34)
MorseArray.push(Index35)

//Function borrowed from: https://stackoverflow.com/a/25352300
function isAlphaNumeric(str){
    var code, i, len;
  
    for (i = 0, len = str.length; i < len; i++) {
      code = str.charCodeAt(i);
      if (!(code > 47 && code < 58) && // numeric (0-9)
          !(code > 64 && code < 91) && // upper alpha (A-Z)
          !(code > 96 && code < 123)) { // lower alpha (a-z)
        return false;
      }
    }
    return true;
  };

var ResultArray = []
//var input = "The quick BROWN fox JUMPED over the lAzY dOg.@!#!@$%$@"
var input = "WhyisthisNoTWoRkInG."
console.log("This is the input: " + input)
input = input.toLocaleLowerCase()
console.log("This should now be lower case:" + input)

/*The problem exists somewhere in this logic block*/
var z=0
while (z < input.length){
    var currentChar = input[z]
    
    //This is causing problems with whitespace detection
    /*if (currentChar === " "){
        console.log("Hey, this is a blank space.")
        ResultArray.push("  ")
    }
    else*/ if(currentChar == "."){
        console.log("Found period. STOP")
        ResultArray.push("STOP")
    }
    else if(isAlphaNumeric(currentChar)){
        //We're now confirmed as an alphanumeric character, go find it in the morse array cipher
        var tempint = 0
        while (tempint < MorseArray.length){ //This is correct, loop through the entire morse array to find the character you want. P!=NP
            if ((MorseArray[tempint]).Name === currentChar){ //THE PROPERTY NAME HAS TO BE CAPITALIZED. BECAUSE REASONS. 
                console.log("Hey, found a match in morse array for: " + currentChar)
                ResultArray.push(MorseArray[tempint].MorseValue) //THIS WAS A PROBLEM HERE
                ResultArray.push(" ")
            }
            else{
                console.log("Did not find " + currentChar + " in morse array")
            }
        tempint += 1    
        }
    }
    z += 1
} 

var tempint2 = 0
while(tempint2 < ResultArray.length){
    console.log(ResultArray[tempint2].MorseValue) //Are we actually pushing to the ResultArray a character object???
    tempint2 += 1
}

console.log("Baby, I'm 40% titanium.")
