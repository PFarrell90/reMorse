#Define Char class
class Char():
    def __init__(self):
        self.Name = None
        self.MorseValue = None

MorseArray = []

#Character objects (alpha-numeric a-z, 0-9)
Index0 = Char(); Index0.Name = "a"; Index0.MorseValue = ".-"
Index1 = Char(); Index1.Name = "b"; Index1.MorseValue = "-..."
Index2 = Char(); Index2.Name = "c"; Index2.MorseValue = "-.-."
Index3 = Char(); Index3.Name = "d"; Index3.MorseValue = "-.."
Index4 = Char(); Index4.Name = "e"; Index4.MorseValue = "."
Index5 = Char(); Index5.Name = "f"; Index5.MorseValue = "..-."
Index6 = Char(); Index6.Name = "g"; Index6.MorseValue = "--."
Index7 = Char(); Index7.Name = "h"; Index7.MorseValue = "...."
Index8 = Char(); Index8.Name = "i"; Index8.MorseValue = ".."
Index9 = Char(); Index9.Name = "j"; Index9.MorseValue = ".---"
Index10 = Char(); Index10.Name = "k"; Index10.MorseValue = "-.-"
Index11 = Char(); Index11.Name = "l"; Index11.MorseValue = ".-.."
Index12 = Char(); Index12.Name = "m"; Index12.MorseValue = "--"
Index13 = Char(); Index13.Name = "n"; Index13.MorseValue = "-."
Index14 = Char(); Index14.Name = "o"; Index14.MorseValue = "---"
Index15 = Char(); Index15.Name = "p"; Index15.MorseValue = ".--."
Index16 = Char(); Index16.Name = "q"; Index16.MorseValue = "--.-"
Index17 = Char(); Index17.Name = "r"; Index17.MorseValue = ".-."
Index18 = Char(); Index18.Name = "s"; Index18.MorseValue = "..."
Index19 = Char(); Index19.Name = "t"; Index19.MorseValue = "-"
Index20 = Char(); Index20.Name = "u"; Index20.MorseValue = "..-"
Index21 = Char(); Index21.Name = "v"; Index21.MorseValue = "...-"
Index22 = Char(); Index22.Name = "w"; Index22.MorseValue = ".--"
Index23 = Char(); Index23.Name = "x"; Index23.MorseValue = "-..-"
Index24 = Char(); Index24.Name = "y"; Index24.MorseValue = "-.--"
Index25 = Char(); Index25.Name = "z"; Index25.MorseValue = "--.."
Index26 = Char(); Index26.Name = "0"; Index26.MorseValue = "----"
Index27 = Char(); Index27.Name = "1"; Index27.MorseValue = ".---"
Index28 = Char(); Index28.Name = "2"; Index28.MorseValue = "..--"
Index29 = Char(); Index29.Name = "3"; Index29.MorseValue = "...-"
Index30 = Char(); Index30.Name = "4"; Index30.MorseValue = "...."
Index31 = Char(); Index31.Name = "5"; Index31.MorseValue = "...."
Index32 = Char(); Index32.Name = "6"; Index32.MorseValue = "-..."
Index33 = Char(); Index33.Name = "7"; Index33.MorseValue = "--.."
Index34 = Char(); Index34.Name = "8"; Index34.MorseValue = "---."
Index35 = Char(); Index35.Name = "9"; Index35.MorseValue = "----"



#x = range(36)
#for n in x:
#    print(n)

#for n in x:
#    MorseArray.append(Index[n)]pyt
 

#print(MorseArray)

##Character Names
#Index0.Name = "a"
#Index1.Name = "b"
#Index2.Name = "c"
#Index3.Name = "d"
#Index4.Name = "e"
#Index5.Name = "f"
#Index6.Name = "g"
#Index7.Name = "h"
#Index8.Name = "i"
#Index9.Name = "j"
#Index10.Name = "k"
#Index11.Name = "l"
#Index12.Name = "m"
#Index13.Name = "n"
#Index14.Name = "o"
#Index15.Name = "p"
#Index16.Name = "q"
#Index17.Name = "r"
#Index18.Name = "s"
#Index19.Name = "t"
#Index20.Name = "u"
#Index21.Name = "v"
#Index22.Name = "w"
#Index23.Name = "x"
#Index24.Name = "y"
#Index25.Name = "z"
#Index26.Name = "0"
#Index27.Name = "1"
#Index28.Name = "2"
#Index29.Name = "3"
#Index30.Name = "4"
#Index31.Name = "5"
#Index32.Name = "6"
#Index33.Name = "7"
#Index34.Name = "8"
#Index35.Name = "9"

#MorseValues
#Index0.MorseValue = ".-"
#Index1.MorseValue = "-..."
#Index2.MorseValue = "-.-."
#Index3.MorseValue = "-.."
#Index4.MorseValue = "."
#Index5.MorseValue = "..-."
#Index6.MorseValue = "--."
#Index7.MorseValue = "...."
#Index8.MorseValue = ".."
#Index9.MorseValue = ".---"
#Index10.MorseValue = "-.-"
#Index11.MorseValue = ".-.."
#Index12.MorseValue = "--"
#Index13.MorseValue = "-."
#Index14.MorseValue = "---"
#Index15.MorseValue = ".--."
#Index16.MorseValue = "--.-"
#Index17.MorseValue = ".-."
#Index18.MorseValue = "..."
#Index19.MorseValue = "-"
#Index20.MorseValue = "..-"
#Index21.MorseValue = "...-"
#Index22.MorseValue = ".--"
#Index23.MorseValue = "-..-"
#Index24.MorseValue = "-.--"
#Index25.MorseValue = "--.."
#Index26.MorseValue = "----"
#Index27.MorseValue = ".---"
#Index28.MorseValue = "..--"
#Index29.MorseValue = "...-"
#Index30.MorseValue = "...."
#Index31.MorseValue = "...."
#Index32.MorseValue = "-..."
#Index33.MorseValue = "--.."
#Index34.MorseValue = "---."
#Index35.MorseValue = "----"