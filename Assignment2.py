                          # ******Assignment 2*********
print("                 Assignment 2")
print("\n")


# *******Question 1*******


print('Question 1 \n')

#Value to input_string
input_string = 'Python is a case sensitive language'

#Length of input_string
print("\nPart a ")
print(f"Length of Input String = {len(input_string)}")

# Reverse order.
print("\nPart b")
print(input_string[::-1])


# Slice function
print("\nPart c")
sliced_string = input_string[10:26]
print(sliced_string)


# replacing and printing.
print("\nPart d")
new_string = input_string.replace("a case sensitive", "object oriented")
print(new_string)


# Index of substring "a"
print("\nPart e")
print(input_string.index("a"))


# Remove White spaces
print("\nPart f")
print(input_string.replace(" ", ""))
print("\n")


# *******Question 2*******


print("Question 2\n")

# Initializing variables.
B1 = "Namit Kulshrestha"                # B1 is Name 
B2 = "21105025"                         # B2 is SID
B3 = "ECE"                              # B3 is Department
B4 = "9.9"                              # B4 is CGPA

print(f" Hey, {B1.title()} here! \n My SID is {B2} \n I am from {B3} and my CGPA is {B4}")
print("\n")


# *******Question 3*******


print("Question 3 \n")

a = 56
b = 10

print(" a&b : ", a & b)
print(" a|b : ", a | b)
print(" a^b : ", a ^ b)

# Left shift both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)

# Right shift a with 2 bits and b with 4 bits.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 4)
print("\n")


# *******Question 4*******


print("Question 4 \n")
print("Enter the numbers to find highest number")

# Input of 3 numbers from user
a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd no. : "))

# Finding the highest number
if a > b:
    if a > c:
        highest_number = a
    else:
        highest_number = c

if b > a:
    if b > c:
        highest_number = b
    else:
        highest_number = c


print(f"Highest no. = {highest_number}")
print("\n")


# *******Question 5*******


print("Qustion 5 \n")

# taking input string from the user.
M1 = input("Enter input string: ")                  # M1 is input string

if "name" in M1:
    print("Yes")
else:
    print("No")
print("\n")


# *******Question 6*******


print("Question 6\n")
print("Enter the numbers to check whether the triangle is possible or not")

# Input of 3 numbers from user
a = int(input("Enter 1st length : ")) 
b = int(input("Enter 2nd length : "))
c = int(input("Enter 3rd length : "))

# checking condition for triangle.
if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")
