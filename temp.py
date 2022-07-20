MyVar = ["A", "bob", " ", "Delta"]

i=0
while i < (len(MyVar)):
    print (MyVar[i])
    if (MyVar[i] == " "):
     print ("^ And this is a blank space!")

    i += 1


#MyVar = "!@##$@"
#MyVar2 = "abcd01234"
#
#val = MyVar2.isalnum()
#print (val)

#class Char():
#    def __init__(self):
#        self.Name = None
#        self.MorseValue = None
#
#
#MyVar = Char(); MyVar.Name = "Mike"; MyVar.MorseValue = "."
#
#print((MyVar.Name),(MyVar.MorseValue))