# # qn 1 

# number=int(input("enter a number:"))
# if number>1:
#     print("positive number")
# elif number<0:
#     print("negative number")
# else:
#     print("zero")    

# # 2 qn

# number = int(input("enter a number:"))
# if number % 2 == 0:
#     print("even number")
# else:
#     print("odd numbers")    


# # qn 3

# number=int(input("enter your age:"))
# if number>=18:
#     print("your eligible")
# else:
#     print("you are not eligible")

# # 4 qn

# a=int(input("enter a number"))
# b=int(input("enter a number"))

# if a>b:
#     print("a is big")
# elif b>a:
#     print("b is big")

# # 5 qn

# marks = int(input("enter your marks:"))
# if marks>40:
#     print("Pass")
# else:
#     print("Fail")    

# # 6 qn

# day=int(input("enter any number"))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day== 3:
#     print("wednesday")  
# elif day== 4:
#     print("Thursday")
# elif day== 5:
#     print("Friday")  
# elif day== 6:
#     print("Saturday")  
# elif day == 7:
#     print("Sunday")    
# else:
#     print("invalid input")  


# # nested version

# day = int(input("Enter any number (1-7): "))

# days = ["Invalid input", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# print(days[day] if 1 <= day <= 7 else days[0])

# # 7 qn








# # 8 qn 

# month = int(input("Enter a number 1-12:"))

# months=["invalid", "january","february","march", "april", "may", "june", "july","august", "september", "october", "november", "december"]

# print(months[month] if 1<= month <=12 else months[0]
# )

# # medium

# # 1 qn

# a = float(input())
# b = float(input())
# c = float(input())

# if a>b and a>c:
#     print("a is greatest")
# elif b>a and b>c:
#     print("b is greatest")
# else:
#     print("c is greatest")    


# # 2


# year = int(input("enter a number"))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("yooo! it's leap year")
# else:
#     print("it's not a leap year")   

 
# year = int(input())

# print("its is leap year") if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else print("not a leap year")

# #  3.
# word = input("enter any input")


# if len(word) == 1 and word.isalpha():
#     if word.lower() in 'aeiou':
#         print("it is vowel")
#     else:
#         print("it is consonant")
# else:
#     print("neither")   
     
    


# 4qn

# marks = int(input())

# if marks >= 90 and marks<= 100:
#     print("Grade A")
# elif marks >= 80 and marks <= 89:
#     print("Grade B")
# elif marks >= 70 and marks <= 79:
#     print("Grade c")
# else:
#     print("Fail")    



# # 5 qn

# a = float(input())
# b = float(input())
# c = float(input())

# if (a+b)>c and (b+c)>a and (c+a)>b:
#     print("its triangle")
# else:
#     print("it is not a triangle")    

# n=0
# for i in range(1,20):
#     n=n+i
#     print(n)

# n= 10
# print((n * (n+1)/2))
# num1= int(input("enter lower bound"))
# num2= int(input("enter upper bound"))

# for p in range(num1,num2+1):
#     count=0
#     for i in range(1, p+1):
#         if p % i==0:
#             count+=1

#     if count==2:
#         print(p, "is prime")
#     else:
#         print(p,"not prime")          
#   


# num = int(input("enter number"))

# while True:
#     num +=1
#     count=0
#     for i in range(1, num+1):
#         if num % i==0:
#             count+=1

#     if count==2:
#         print(num)
#         break

# lower_range = 100
# upper_range = 10000

# for i in range(lower_range, upper_range + 1):
#     temp = i

#     temp_str = len(str(i))

#     sum = 0
#     while temp> 0:
#         rem = temp % 10
#         sum += rem ** temp_str
#         temp = temp // 10
    
#     if i == sum:
#         print(i, "Is Armstrong")


# year = int(input())
# next_year= 0
# is_leap_year = 0
# print("its is leap year") if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else print("not a leap year") 

# year = int(input("Enter a year: "))

# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
    
   
#     next_year = year + 1
#     while not is_leap_year(next_year):
#         next_year += 1
    
#     print(f"The next leap year is: {next_year}")
    


# def check_if_prime(num1):
#     if num1 <= 1:
#         return False
#     for i in range(2, num1):
#         if num1 % i == 0:
#             return False
#     return True
# print(num1," is prime") 


# def check_if_armstrong(num1):
    
#     temp = num1
#     res = 0
#     while temp > 0:
#         rem = temp % 10
#         res += rem ** len(str(num1))
#         temp = temp // 10
    
#     return res == num1


# def fibonacci(n):
#     # Create a list to store the Fibonacci sequence
#     fib_sequence = []
    
#     # Initialize the first two Fibonacci numbers
#     a, b = 0, 1
    
#     # Loop to generate the Fibonacci sequence
#     for _ in range(n):
#         fib_sequence.append(a)  # Append the current number to the list
#         a, b = b, a + b  # Update a and b to the next two Fibonacci numbers
    
#     return fib_sequence

# num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci(num_terms)}")


# def fibonacci(n):

#     fib_sequence =[]
#     a,b = 0,1

#     for i in range(n):
#         fib_sequence.append(n)
#         a,b = b, a+b

#     return fib_sequence

# num = int(input("enter a number"))
# print(num)



