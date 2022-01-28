#program my dog
class mydog():
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("woof")
    def printname(self):
        print("My name is: {}".format(self.name))
dogname=mydog("browny")
dogname.talk()
dogname.printname()
