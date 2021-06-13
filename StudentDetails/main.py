from Student import *

u_id = int(input("Enter the student id\n"))
username = input("Enter the student's username\n")
password = input("Enter the password\n")
name = input("Enter the name of the student\n")
address = input("Enter the address\n")
city = input("Enter the city\n")
pincode = int(input("Enter the pincode\n"))
contact_number = int(input("Enter the contact number\n"))
email = input("Enter the email id\n")

obj1 = Student(u_id, username, password, name, address, city, pincode, contact_number, email)
print(obj1)
