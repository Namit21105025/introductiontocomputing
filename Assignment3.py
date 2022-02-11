# ***************** Question - 1 *****************

print("\t \t \t Question 1 \n")

# Taking string input from the user to count the letters of the string.
user_input = input("Enter the string: ")

# Converting upercase letters to lower case and storing it in list.
user_input = user_input.lower()

print()

count_dict = {}               # Empty disc for counting words.

# Spliting the string in the list
user_words = user_input.split(" ")

# Checking if input string is a single word or not so that we can count different words of the string 
if len(user_words) == 1:
    user_words = user_input

# For loop is used to count the occurance of words and characters.
for word in user_words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict.update({word : 1})

# Result.
if len(user_input) == 0:
    print("No word or sentence found.")
else:
    print("Number of each word/character in string is:" ,count_dict , "\n")



#########################################################################################
# ***************** QUESTION - 2 ***************** 

print("\t \t \t Question 2 \n")

# Taking input from the user.
date = int(input("Enter the date: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
print()

# Calculating the next date.
if (1 <= month <= 12) and (1 <= date <= 31) and (1800 <= year <= 2025):

#Calculating next date for the month of 31 days.
    if month in (1,3,5,7,8,10):
        if date < 31:
            date += 1
        else:
            date = 1
            month += 1

# Calculating next date for the month of 30 days.
    elif month in (4,6,9,11):
        if date < 30:
            date += 1
        else:
            date = 1
            month += 1

# February with 28 days
    elif month == 2:

# Leap year
        if year % 4 == 0:
            if date < 29:
                date += 1
            else:
                date = 1
                month += 1
        else:
            if date < 28:
                date += 1
            else:
                date = 1
                month += 1

# Next date for december month
    else:
        if date < 31:
            date += 1
        else:
            date = 1
            month = 1
            year += 1

# Solution to the next date 
    if date == 1 and month == 1 and year == 2026:
        print("Date is out of range.")
    else:
        print(f"Next day is: {date}/{month}/{year}")
else:
# If date is invalid
    print("Invalid Date.")
print("\n")    



#########################################################################################
# ***************** Question - 3 *****************

print("\t \t \t Question 3 \n")

# Taking given and output list from the user
given_list = []
output_list = []

max_input = int(input("Enter the total number of terms you gonna enter: "))
print()
for i in range(max_input):
    tmp_num = int(input(f"Enter the {i + 1} number: "))
    given_list.append(tmp_num)
print()

# for loop is used to calculate sqaure and adding it in tuple.
for num in given_list:
    temp_tuple = (num,num*num)
    output_list.append(temp_tuple)

# Result
print(output_list)
print("\n")



#########################################################################################
# ***************** QUESTION - 4 *****************

print("\t \t \t Question 4 \n")

# Taking input from the user:
grade_num = int(input("Enter the grade number: "))
print()

# Validity check
if 4 <= grade_num <= 10:

    # Grade corresponding to the input.
    if grade_num == 10:
        print("Your grade is 'A+' and Outstanding Performance")
    elif grade_num == 9:
        print("Your grade is 'A' and Excellent Performance")
    elif grade_num == 8:
        print("Your grade is 'B+' and Very Good Performance")
    elif grade_num == 7:
        print("Your grade is 'B' and Good Performance")
    elif grade_num == 6:
        print("Your grade is 'C+' and Average Performance")
    elif grade_num == 5:
        print("Your grade is 'C' and Below Average Performance")
    else:
        print("Your grade is 'D' and Poor Performance")

else:

# If grade is invalid
    print("grade is Invalid.")
print("\n")



#########################################################################################
# ***************** Question - 5 *****************

print("\t \t \t Question 5 \n")

print(" Printing the given pattern : \n")
# Letters to be printed
abcd = "ABCDEFGHIJK"
# Forming the list of letters
list_abcd = []
for i in abcd:
    list_abcd.append(i)

# While loop is used to print the required rows.
k = 1
while k <= 6:
    # printing 1st row intially when k=1
    for el in list_abcd:
        print(el, end="")
    # forming second row elements to be printed
    list_abcd.pop(len(list_abcd) - 1)         # removing last element of list
    list_abcd.pop(len(list_abcd) - 1)         # removing last element of list
    list_abcd.insert(0, " ")                  # insertind space
    print()                                   # changing line using print()
    k = k + 1
print("\n")



#########################################################################################
# ***************** Question - 6 *****************

print("\t \t \t Question 6 \n")
                  
# 1st run
repeat="Y"
                  
# Empty dictionary
dic={}
dic2={}
                  
# List containing Y or N
liste=["Y","y","n","N"]
                  
# Main code
while repeat=="Y" or repeat=="y":
    # Taking input name and sid from the user
    
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
        # Updating dictionary with 'sid':'name'
        dic.update({sid: name})
        # Updating dictionar 2 with 'name':'sid'
        dic2.update({name:sid})
        # Asking if want to enter more input or not
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a

# Printing the dictionary
print("\n Question 6(a) \n")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)

# b

# Sorting according to name
print("\n Question 6(b) \n")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c

# Sorting according to SID
print("\n Question 6(c) \n")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)

# d

print("\n Question 6(d) \n")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# Printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")
print("\n")



#########################################################################################
# ***************** QUESTION - 7 *****************

print("\t \t \t Question 7 \n")

# rec function to print fibonacci series
def fibonacci_seq(n):
    if n <= 1:
       return n
    return(fibonacci_seq(n-1) + fibonacci_seq(n-2))

# Average of fibonacci series
sum = 0
avg_counter = 0

while True:

    # Taking input from the user to print max number of terms
    max_num_of_terms = int(input("Enter the the max number of terms you want to print: "))
    print()

    # If max number is negative -:
    if max_num_of_terms <= 0:
        print("Plese enter a positive integer")

    # Printing fibonacci series
    else:

        print(f"Fibonacci sequence with {max_num_of_terms} terms:")

        for count in range(max_num_of_terms):
            temp = fibonacci_seq(count)
            sum += temp
            avg_counter += 1
            print(temp)
        
        print()
        break

# Printing average of fibonacci series
average_fab_seq = sum/avg_counter
print("Average of fab series is: ",average_fab_seq)
print("\n")



#########################################################################################
# ***************** Question - 8 *****************

print(" \t \t \t Question 8 \n")

# Given sets
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

# Intersection of set 1 & 2 is to be subtracted from union of both sets

print("\n Question 8(a) \n")
set_notboth=Set1^Set2
print(f"set with elements not common in both is {set_notboth}")

# Intersection of three sets and 2 at a time to be subtracted from total union of these three sets

print("\n Question 8(b) \n")
set_onlyinone=Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_onlyinone}")

# Intersection of two at a time and subtract intersection of three of these sets

print("\n Question 8(C) \n")
set_onlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_onlyintwo}")

# Simply we write 1-10 and subtract set 1 from this

print("\n Question 8(d) \n")
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
not_common_1=new_set1- Set1
print(f"set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")

# Simply we write 1-10 and subtract set 1,2,3 from this

print("\n Question 8(e) \n")
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_common_2=new_set2 - (Set1|Set2|Set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}")






    
