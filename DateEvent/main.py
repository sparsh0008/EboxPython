from Event import *

name = input("Enter the name:\n")
dob = input("Enter the DOB(dd/MM/yyyy):\n")

obj1 = Event(name, dob)
R = obj1.checkDate()

if obj1.flag == 'even':
    if not obj1.printFlag:
        print("You are offered with the Birthday Bash on {0} {1} of this year".format(self.mName, self.date))
else:
    if not obj1.printFlag:
        print("You are not offered with the Birthday Bash")
