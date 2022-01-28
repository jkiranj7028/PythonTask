class student(object):
    def __init__(self, name, branch, year):
        self.name=name
        self.branch=branch
        self.year=year
        print("A student object i s created")
    def print_details(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("year:",self.year)
obj1=student("kiran", "EEE", 2005)
obj1.print_details()
