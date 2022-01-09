#Assignment 1

print("NAMIT, 21105025, ECE")
print("\n")
      
#1st Program

print("      First program")

#********Input from user***********
numb1=int(input("Enter the first number \n"))
numb2=int(input("Enter the second number \n"))
numb3=int(input("Enter the third number \n"))

#*******Formula***********
avg=(numb1+numb2+numb3)/3

print("The avg of number is: \n",avg)
print("\n")
print("\n")


#2nd Program

print("      Second Program")

Tax_Rate = 0.20                    #Tax rate is 20%
Standard_Deduction = 10000         #It is in Dollor ($)
Dependent_Deduction = 3000         #It is in Dollor ($)

#********Input from user***********
Gross_Income = int(input("Enter your Gross Income in $ to the nearest penny: \n"))
Number_of_Dependents = int(input("Enter the number of dependents: \n"))

#***********Formula****************
Taxable_Income = Gross_Income-Standard_Deduction-(Dependent_Deduction*Number_of_Dependents)

Tax = Taxable_Income*Tax_Rate

if Tax<0:
    print("Your income tax is 0$")
else:
    print("Your tax is: \n",Tax)
    
print("\n")
print("\n")



#3rd Program

print("      Third Program")

#********Input from user***********
A1 = int(input("Enter your SID: \n"))              #A1 is student SID
A2 = input("Enter your Name: \n")                  #A2 is the student name
A3 = input("Enter your Gender (M,F,U): \n")        #A3 is the student Gender M-Male , F-Female , U-other
A4 = input("Enter your Course Name: \n")           #A4 is the student course name
A5 = float(input("Enter your CGPA: \n"))           #A5 is the student CGPA

#********LIST*********
Student = [A1, A2, A3, A4, A5]

print(Student)
print("\n")
print("\n")


#4th Program

print("      Fourth Program")

#********Input from user***********
B1 = float(input("Enter the marks of Student 1: \n"))                  #B1 is the Marks of first student***********
B2 = float(input("Enter the marks of Student 2: \n"))                  #B2 is the Marks of second student***********
B3 = float(input("Enter the marks of Student 3: \n"))                  #B3 is the Marks of third student***********
B4 = float(input("Enter the marks of Student 4: \n"))                  #B4 is the Marks of fourth student***********
B5 = float(input("Enter the marks of Student 5: \n"))                  #B5 is the Marks of fifth student***********

#********LIST*********
Marks = [B1,B2,B3,B4,B5]
Marks.sort()

print(Marks)
print("\n")
print("\n")


#5th Program

print("      Fifth program")

print("The list of color is:")
print("['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']")
print("\n")

#(a)

print("(a)")

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color.remove('Black')

print("Output first is: \n",color)
print("\n")

#(b)

print("(b)")

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color[3:5] = ["Purple"]

print("Output second is: \n",color)

