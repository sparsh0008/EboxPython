from Stall import *

name = input("Enter book name\n")
detail = input("Enter book details\n")
n = int(input("Menu\n1.Use Construtor to initialize\n2.Use setters and getters\n"))

if n == 1:
    p = Stall(name, detail)
    print("Initializing and printing using parameterized Constructor and Str method")
    print("Details of the stall category:")
    print(p.__str__())

elif n == 2:
    p = Stall(name, detail)

    print("Initializing and printing using default Constructor and Setters and Getters")
    print("Details of the stall category:")
    print("Book Name :",p.get_name())
    print("Detail :",p.get_detail())
