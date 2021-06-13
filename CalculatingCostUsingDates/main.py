from HallCalculateCostUsingDate import *

d1 = str(input("Enter Start date\n"))
d2 = str(input("Enter the End date\n"))
cost = int(input("Enter the cost per day\n"))

Obj1 = Hall(d1, d2, cost)
Obj1.no_days()
