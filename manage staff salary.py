class Employee:
    name = ""
    id = ""
    position = ""
    salary = 0
    def __init__(self, name, id, position, salary):
        self.name = name
        self.id = id
        self.position = position
        self.salary = salary
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getposition(self):
        return self.position
    def getsalary(self):
        return self.salary

class Office:
    stafflist = []
    managerlist = []
    officerlist = []
    nostaff = 0
    def addStaffEmployee(self, name, id, position, salary):
        self.stafflist.append(Employee(name, id, position, salary))
        self.nostaff += 1
    def addOfficerEmployee(self, name, id, position, salary):
        self.officerlist.append(Employee(name, id, position, salary))
        self.nostaff += 1
    def addManagerEmployee(self, name, id, position, salary):
        self.managerlist.append(Employee(name, id, position, salary))
        self.nostaff += 1
    def deleteEmployee(self):
        bool = True
        id = input("Input ID[SXXXX]: ")
        for i in range(len(self.stafflist)):
            if self.stafflist[i].getid() == id:
                self.stafflist.pop(i)
                print("Data has been successfully deleted")
                bool = False
        for i in range(len(self.officerlist)):
            if self.officerlist[i].getid() == id:
                self.officerlist.pop(i)
                print("Data has been successfully deleted")
                bool = False
        for i in range(len(self.managerlist)):
            if self.managerlist[i].getid() == id:
                self.managerlist.pop(i)
                print("Data has been successfully deleted")
                bool = False
        if(bool == True):
            print("ID not found")
    def checkID(self, id):
        bool = True
        for i in range(len(self.stafflist)):
            if(id == self.stafflist[i].getid()):
                bool = False
        return bool
    def viewData(self):
        staffsalary = []
        officersalary = []
        managersalary = []
        staffsalarytotal = 0
        officersalarytotal = 0
        managersalarytotal = 0
        for i in range(len(self.stafflist)):
            if (len(self.stafflist) == 0):
                pass
            staffsalary.append(self.stafflist[i].getsalary())
        for i in range(len(self.officerlist)):
            if (len(self.officerlist) == 0):
                pass
            officersalary.append(self.officerlist[i].getsalary())
        for i in range(len(self.managerlist)):
            if (len(self.managerlist) == 0):
                pass
            managersalary.append(self.managerlist[i].getsalary())

        for i in range(len(staffsalary)):
            if (len(staffsalary) == 0):
                pass
            staffsalarytotal += int(staffsalary[i])
        for i in range(len(officersalary)):
            if (len(officersalary) == 0):
                pass
            officersalarytotal += int(officersalary[i])
        for i in range(len(managersalary)):
            if (len(managersalary) == 0):
                pass
            managersalarytotal += int(managersalary[i])

        if(len(staffsalary) != 0):
            staffmean = staffsalarytotal / len(staffsalary)
            print("1. Staff")
            print("Minimum Salary: " + str(min(staffsalary)))
            print("Maximum Salary: " + str(max(staffsalary)))
            print("Average Salary: " + str(staffmean))
        if(len(officersalary) != 0):
            officermean = officersalarytotal/ len(officersalary)
            print("2. Officer")
            print("Minimum Salary: " + str(min(officersalary)))
            print("Maximum Salary: " + str(max(officersalary)))
            print("Average Salary: " + str(officermean))
        if(len(managersalary) != 0):
            managermean = managersalarytotal / len(managersalary)
            print("3. Manager")
            print("Minimum Salary: " + str(min(managersalary)))
            print("Maximum Salary: " + str(max(managersalary)))
            print("Average Salary: " + str(managermean))
        if(len(staffsalary) == 0) and (len(officersalary) == 0) and (len(managersalary) == 0):
            print("There is no existing data")

    def read(self):
        dataid = []
        dataname = []
        dataposition = []
        datasalary = []
        f = open("data.txt", "r")
        for line in f:
            fields = line.split(",")
            if(len(fields) == 0):
                break
            else:
                for i in range(len(fields)):
                    if i % 4 == 0:
                        dataid.append(fields[i])
                    elif i % 4 == 1:
                        dataname.append(fields[i])
                    elif i % 4 == 2:
                        dataposition.append(fields[i])
                    elif i % 4 == 3:
                        datasalary.append(fields[i])
        for i in range(len(dataid)-1):
            if(len(dataid) == 0):
                break
            else:
                if(dataposition[i] == "staff"):
                    office.addStaffEmployee(dataname[i], dataid[i], dataposition[i], datasalary[i])
                elif(dataposition[i] == "officer"):
                    office.addOfficerEmployee(dataname[i], dataid[i], dataposition[i], datasalary[i])
                elif(dataposition[i] == "manager"):
                    office.addManagerEmployee(dataname[i], dataid[i], dataposition[i], datasalary[i])

    def saveandexit(self):
        f = open("data.txt", "w+")
        for i in range(len(self.stafflist)):
            if(len(self.stafflist) == 0):
                break
            f.write(str(self.stafflist[i].getid()) + "," + str(self.stafflist[i].getname()) + "," + str(self.stafflist[i].getposition()) + "," + str(self.stafflist[i].getsalary()) + ",")
        for i in range(len(self.officerlist)):
            if (len(self.officerlist) == 0):
                break
            f.write(self.officerlist[i].getid() + "," + self.officerlist[i].getname() + "," + self.officerlist[
                i].getposition() + "," + str(self.officerlist[i].getsalary()) + ",")
        for i in range(len(self.managerlist)):
            if (len(self.managerlist) == 0):
                break
            f.write(self.managerlist[i].getid() + "," + self.managerlist[i].getname() + "," + str(self.managerlist[
                i].getposition()) + "," + str(self.managerlist[i].getsalary()) + ",")
            f.close()
office = Office()
office.read()
while True:
    print("\tMAIN MENU")
    print("1. NEW STAFF ")
    print("2. DELETE STAFF")
    print("3. VIEW SUMMARY DATA")
    print("4. SAVE AND EXIT")
    print("Select Your Option (1-4) ")
    ui = input()
    if ui == "1":
        flag = False
        while True:
            if flag == True:
                break
            id = input("input your id [SXXXX]: ")
            if (len(id) == 5) and (id[0] == "S") and (
                    id[1:5].isdigit()):
                if office.checkID(id) == True:
                    while True:
                        if flag == True:
                            break
                        name = input("input your name : ")
                        if (len(name) <= 20):
                            while True:
                                if flag == True:
                                    break
                                position = input("choose position [staff/manager/officer] : ")
                                if (position == "staff") or (position == "officer") or (position == "manager"):
                                    while True:
                                        salary = input("Input salary: ")
                                        if flag == True:
                                            break
                                        if position == "staff":
                                            if int(salary) >= 3500000 and int(salary) <= 7000000:
                                                office.addStaffEmployee(name, id, position, salary)
                                                print("Added successfully")
                                                flag = True
                                                break
                                            else:
                                                print("Wrong salary input")

                                        elif position == "officer":
                                            if int(salary) >= 7000001 and int(salary) <= 10000000:
                                                office.addOfficerEmployee(name, id, position, salary)
                                                print("Added successfully")
                                                flag = True
                                                break
                                            else:
                                                print("Wrong salary input")

                                        elif position == "manager":
                                            if int(salary) > 10000000:
                                                office.addManagerEmployee(name, id, position, salary)
                                                print("Added successfully")
                                                flag = True
                                                break
                                            else:
                                                print("Wrong salary input")
                                else:
                                    print("Wrong input of position")
                        else:
                            print("Name length exceed")
                else:
                    print("ID not unique")
                    break
            else:
                print("wrong  format")

    elif ui == "2":
        office.deleteEmployee()
    elif ui == '3':
        office.viewData()
    elif ui == '4':
        office.saveandexit()
        print("Thank you for using this application")
        break
