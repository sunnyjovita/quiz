display_records = {["S0001", "Garry", "Staff", 4500000],
                  ["S0002", "James", "Staff", 5000000],
                  ["S0004", "Judith", "Manager", 10700000],
                   ["S0003", "Yuli", "Officer", 8500000]}
print(display_records)
print("|    ID   |     NAME    |    POSITION    |   SALARY    |")
for item in display_records:
    print("|", item[0], " "*(6-len(item[0])), "|", item[1], " "*(10-len(item[1])), "|", item[2], " "*(13-len(item[2])), "|", item[3], " "*(10-len(str(item[3]))), "|")

class Manager:
    __ID = ""
    __name = ""
    __position = ""
    __salary = 0
    __numberofstaff = 0
    def __init__(self, ID, name, position, salary):
        self.__ID = ID
        self.__name = name
        self.__position = position
        self.__salary = salary
    def getId(self):
        return self.__ID
    def getName(self):
        return self.__name
    def getPosition(self):
        return self.__position
    def getSalary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            pass
    def getNumberofstaff(self):
        return self.getNumberofstaff()
newManager = Manager()
while True:
    print("\tMAIN MENU")
    print("1. NEW STAFF ")
    print("2. DELETE STAFF")
    print("3. VIEW SUMMARY DATA")
    print("4. SAVE AND EXIT")
    print("Select Your Option (1-4) ")
    ui = input()
    if ui == "1":
        name = input("enter your name: ")
        id = input("enter your id: ")
        staff = input("input your position: ")
        amount = str(input("input your salary :"))
        # newManager.
