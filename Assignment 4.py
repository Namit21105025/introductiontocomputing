################################################################# ASSIGNMENT-4 ###################################################################################
print("\t \t \t Assignment 4")
print("\n")



#***** QUESTION-1 *****
# TOWER OF HANOI

print("\t \t \t Question-1 \n")

def Tower_of_Hanoi(n, source, destination, auxillary):
    if n==1:
        print("Move disc 1 from", source, "to", destination)         # only 1 move is required for n=1
    else:
        Tower_of_Hanoi(n-1, source, auxillary, destination)          # moves first (n-1) discs from source peg to auxillary peg
        print("Move disc", n, "from", source, "to", destination)     # moves the largest peg from source peg to destination peg
        Tower_of_Hanoi(n-1, auxillary, destination, source)          # moves the (n-1) pegs in auxillary peg to destination peg

n=int(input("Enter the number of discs: "))
Tower_of_Hanoi(n, 'A', 'B', 'C')                                     # A is peg-1 (source peg), B is peg-2 (destination peg), C is peg-3 (auxillary peg)

print("\n")



#***** QUESTION-2 *****
# PASCAL'S TRIANGLE

print("\t \t \t Question-2 \n")

num=int(input("Enter number of rows: "))

def factorial(n):                   # gives factorial of a number
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

# ITERATIVE METHOD
for i in range(0, num):             # two for loops are applied to give nCr
    for j in range(0, num-i):
        print(" ", end="")
    for j in range (0, i+1):
        print(int(factorial(i)/(factorial(j)*factorial(i-j))), end=" ")               # prints formula of nCr according to Pascal's Triangle
    print()

# RECURSIVE METHOD
def pascal(n, k):
    if(n<0):
        return
    else:
        pascal(n-1, k)                  # recursion gives previous lines of Pascal's triangle
        for i in range(0, k-n):
            print(" ", end="")
        for i in range(0, n):
            print(int(factorial(n-1)/(factorial(i)*factorial(n-1-i))), end=" ")                # give current line of Pascal's Triangle
        print()
pascal(num, num)

print("\n")



#***** QUESTION-3 *****
# BUILT-IN FUNCTIONS

print("\t \t \t Question-3 \n")

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

q=a//b
r=a%b
print("The quotient is", q, "and the remainder is", r)

# PART-(a)
# callable function checks if functions/values are callable or not
print(callable(q))
print(callable(r))

# PART-(b)
# check if values are non-zero or not
print(q!=0)
print(r!=0)

# PART-(c)
my_list=[q, r]+[4, 5, 6]                        # adding elements in list
print(my_list)
my_list=(list(filter(lambda i: i<=4, my_list))) # filters out values  greater than 4
print(my_list)

# PART-(d)
my_set=set(my_list)                             # makes set from list
print(my_set)

# PART-(e)
my_set=frozenset(my_set)                        # makes set immutable
print(my_set)       

# PART-(f)
max_num=max(my_set)                             # finds max value
print(max_num)
print(hash(max_num))                            # finds hash value
        
print("\n")



#***** QUESTION-4 *****
# CLASS STUDENT

print("\t \t \t Question-4 \n")

class Student():                # Creating class named student.

    def __init__(self,name,rollno):         # initilizing name and roll number
        self.name = name
        self.rollno = rollno
        print(f"Object created for {self.name}")

    def show_info(self):                    # Details of student
        print(f'The name of the student is {self.name}')
        print(f'The roll number of {self.name} is {self.rollno}')

    def __del__(self):                      # Destructor
        print(f"Destructor deleted {self.name}'s record.")

# Creating objects 
student_1 = Student("Namit Kulshrestha", 21105025)
student_2 = Student("Ayush kher", 21105001)
student_3 = Student("Abhinav Aggarwal", 21103030)
print()

# Details of students
student_1.show_info()
print("\n")
student_2.show_info()
print("\n")
student_3.show_info()
print('\n')

# Calling destructor.
del student_1
del student_2
del student_3


print("\n")



#***** QUESTION-5 *****
# CLASS EMPLOYEE

print("\t \t \t Question-5 \n")

class factory():                        # Creating a class names factory.

    def __init__(self,name,salary):     # Storing data of employees
        self.name = name
        self.salary = salary
        print(f"Object created named {self.name}.")

    def show_info(self):                # Data of employees
        print("\tShowing info of the employee.")
        print(f"Name of the employee working in this factory is {self.name}")
        print(f"Salary of {self.name} is {self.salary}.")

    def update_salary(self,new_salary): # Update the salary of employee
        self.salary = new_salary
        print(f"Updated salary of the employee {self.name} is {self.salary}\n")

    def __del__(self):                  # Deleting data of employee
        print(f"Record of the employee {self.name} is deleted.")
    
# Employees
Mehak = factory('Mehak', 40000)
Ashok = factory("Ashok", 50000)
Viren = factory('Viren', 60000)
print()

# DATA of employees
Mehak.show_info()
print()
Ashok.show_info()
print()
Viren.show_info()
print()

# Updating salary of employee
print("Updating mehak's salary.")
Mehak.update_salary(70000)

# Removing data of employee
print("Calling destructor to delete viren's record.")
del Viren

print("\n")



#***** QUESTION-6 *****
# ANAGRAM TEST

print("\t \t \t Question-6 \n")

george_word=input("Enter George's word: ")
barbie_word=input("Enter Barbie's word: ")

def anagrams(s):                            # function to find list of anagrams
    if s=="":
        return [s]
    else:
        ans=[]                              # list of anagrams
        for w in anagrams(s[1:]):           # iterates over anagrams of tail of the string
            for pos in range(len(w)+1):     # puts first letter in different positions in the anagrams of the remaining letters
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans

correct_words=anagrams(george_word)
if barbie_word in correct_words:            # checks if Barbie's word is an anagram of George's word
    print("Friendship is True.")
else:
    print("Friendship is Fake.")
