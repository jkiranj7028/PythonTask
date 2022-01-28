class student():
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year
        print("a student bject is created.")
    def print_details(self):
        print("Name: ", self.name)
        print("Branch: ", self.branch)
        print("Year: ", self.year)
obj1=student("Kiran","EEE", 2005)
obj1.print_details()

        