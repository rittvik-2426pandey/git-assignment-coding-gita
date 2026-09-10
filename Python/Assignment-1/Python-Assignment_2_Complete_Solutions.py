# Assignment-2 — Complete Solutions
# Topics: Type Casting, Arithmetic Operators, Digit Extraction, Debugging

# Question 1 — String to Integer
age = "25"
age = int(age)
print(age)
print(type(age))

# Question 2 — String to Float
marks = "75.5"
marks = float(marks)
print(marks)
print(type(marks))

# Question 3 — Integer to Float
number = 50
number = float(number)
print(number)
print(type(number))

# Question 4 — Float to Integer
marks = 85.9
marks = int(marks)
print(marks)
print(type(marks))

# Question 5 — Integer to String
roll_number = 101
roll_number = str(roll_number)
print(roll_number)
print(type(roll_number))

# Question 6 — Multiple Conversions
value1 = int("18")
value2 = float("92.5")
value3 = str(100)
value4 = int(45.8)
print(value1, type(value1))
print(value2, type(value2))
print(value3, type(value3))
print(value4, type(value4))

# Question 7 — Predict the Output
a = "20"
b = int(a)
c = 10.8
d = int(c)
e = 25
f = str(e)
print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))

# Question 8 — Debug Type Casting
age = "19"
new_age = int(age) + 1
print("Age:", new_age)

# Question 9 — Marks Conversion
marks = "85"
final_marks = int(marks) + 5
print("Final Marks:", final_marks)

# Question 10 — Price Conversion
price = "1499.50"
total_amount = float(price) + 99.50
print("Total Amount:", total_amount)

# Question 11 — Basic Arithmetic
a = 20
b = 6
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# Question 12 — Predict the Output
a = 17
b = 5
print(a / b)
print(a // b)
print(a % b)
# / gives division, // gives the whole-number floor result, and % gives the remainder.

# Question 13 — Operator Precedence
result = 10 + 5 * 2
print(result)
result = (10 + 5) * 2
print(result)

# Question 14 — More Precedence Practice
result = 20 - 4 * 3 + 2
print(result)
result = 20 - (4 * 3) + 2
print(result)

# Question 15 — Power Operator
print(2 ** 3)
print(3 ** 2)
print(10 ** 2)
side = 5
area = side ** 2
print("Area of Square:", area)

# Question 16 — Shopping Bill
notebook = 80
pen = 20
pencil = 10
total_amount = notebook + pen + pencil
print("Total Amount:", total_amount)

# Question 17 — Multiple Quantities
notebook_cost = 3 * 50
pen_cost = 2 * 15
calculator_cost = 1 * 500
total_bill = notebook_cost + pen_cost + calculator_cost
print("Notebook Cost:", notebook_cost)
print("Pen Cost:", pen_cost)
print("Calculator Cost:", calculator_cost)
print("Total Bill:", total_bill)

# Question 18 — Complete Groups and Remainder
students = 47
group_size = 5
complete_groups = students // group_size
students_left = students % group_size
print("Complete Groups:", complete_groups)
print("Students Left:", students_left)

# Question 19 — Average Marks
python_marks = 85
math_marks = 78
physics_marks = 92
total_marks = python_marks + math_marks + physics_marks
average_marks = total_marks / 3
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# Question 20 — Percentage
english = 78
mathematics = 85
python_marks = 92
physics = 81
chemistry = 74
total_marks = english + mathematics + python_marks + physics + chemistry
percentage = total_marks / 500 * 100
print("Total Marks:", total_marks)
print("Percentage:", percentage)

# Question 21 — Ones Digit
number = 583
ones_digit = number % 10
print("Ones Digit:", ones_digit)

# Question 22 — Tens Digit
number = 583
tens_digit = (number // 10) % 10
print("Tens Digit:", tens_digit)

# Question 23 — Hundreds Digit
number = 583
hundreds_digit = number // 100
print("Hundreds Digit:", hundreds_digit)

# Question 24 — Three-Digit Number Analyzer
number = 746
ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100
print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)

# Question 25 — Four-Digit Number
number = 5829
ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000
print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)
print("Thousands Digit:", thousands_digit)

# Question 26 — Sum of Digits
number = 583
ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100
digit_sum = ones + tens + hundreds
print("Sum of Digits:", digit_sum)

# Question 27 — Four-Digit Sum
number = 4726
ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000
digit_sum = ones + tens + hundreds + thousands
print("Sum of Digits:", digit_sum)

# Question 28 — Product of Digits
number = 234
ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100
digit_product = ones * tens * hundreds
print("Product of Digits:", digit_product)

# Question 29 — Reverse a Three-Digit Number
number = 583
ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100
reversed_number = ones * 100 + tens * 10 + hundreds
print("Original Number:", number)
print("Reversed Number:", reversed_number)

# Question 30 — Reverse a Four-Digit Number
number = 4726
ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = number // 1000
reversed_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands
print("Original Number:", number)
print("Reversed Number:", reversed_number)

# Question 31 — Place Value
number = 5834
thousands = (number // 1000) * 1000
hundreds = ((number // 100) % 10) * 100
tens = ((number // 10) % 10) * 10
ones = number % 10
print("Thousands Place:", thousands)
print("Hundreds Place:", hundreds)
print("Tens Place:", tens)
print("Ones Place:", ones)

# Question 32 — Difference Between First and Last Digit
number = 583
hundreds_digit = number // 100
ones_digit = number % 10
difference = hundreds_digit - ones_digit
print("Difference:", difference)

# Question 33 — Digit Extraction Debugging
number = 583
ones = number % 10
print("Ones Digit:", ones)

# Question 34 — Four-Digit Extraction
number = 9365
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10
print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)

# Question 35 — Build a Number
hundreds = 5
tens = 8
ones = 3
number = hundreds * 100 + tens * 10 + ones
print("Number:", number)

# Question 36 — Simple Interest
principal = 10000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

# Question 37 — Rectangle
length = 15
width = 8
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)

# Question 38 — Circle
radius = 7
pi = 3.14
area = pi * radius ** 2
print("Area:", area)

# Question 39 — Temperature Conversion
celsius = 35
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)

# Question 40 — Time Conversion
total_seconds = 367
minutes = total_seconds // 60
seconds = total_seconds % 60
print("Minutes:", minutes)
print("Seconds:", seconds)

# Question 41 — Hours, Minutes and Seconds
total_seconds = 7384
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

# Question 42 — Salary Calculation
basic_salary = 25000
hra = 5000
travel_allowance = 2500
tax_deduction = 3000
gross_salary = basic_salary + hra + travel_allowance
net_salary = gross_salary - tax_deduction
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)

# Question 43 — Travel Cost
distance = 120
mileage = 20
fuel_price = 100
fuel_required = distance / mileage
total_fuel_cost = fuel_required * fuel_price
print("Fuel Required:", fuel_required)
print("Total Fuel Cost:", total_fuel_cost)

# Question 44 — Shopping Discount
price = "2500"
discount = "10"
price = float(price)
discount = float(discount)
discount_amount = price * discount / 100
final_price = price - discount_amount
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)

# Question 45 — String Numbers
price = "1200"
quantity = "4"
price = int(price)
quantity = int(quantity)
total_price = price * quantity
print("Price:", price)
print("Quantity:", quantity)
print("Total Price:", total_price)

# Question 46 — Student Result
python_marks = "85"
math_marks = "78"
physics_marks = "91"
python_marks = int(python_marks)
math_marks = int(math_marks)
physics_marks = int(physics_marks)
total_marks = python_marks + math_marks + physics_marks
average_marks = total_marks / 3
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# Question 47 — Bill with Tax
price = "1500"
quantity = "2"
tax_rate = "5"
price = int(price)
quantity = int(quantity)
tax_rate = float(tax_rate)
subtotal = price * quantity
tax_amount = subtotal * tax_rate / 100
final_bill = subtotal + tax_amount
print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)

# Question 48 — Discount + GST
price = 2000
discount = 15
gst = 18
discount_amount = price * discount / 100
price_after_discount = price - discount_amount
gst_amount = price_after_discount * gst / 100
final_price = price_after_discount + gst_amount
print("Discount Amount:", discount_amount)
print("Price After Discount:", price_after_discount)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)

# Question 49 — Debug the Billing Program
price = "500"
quantity = 3
price = int(price)
total = price * quantity
print("Total:", total)

# Question 50 — Debug the Marks Program
marks1 = "80"
marks2 = "75"
marks3 = "90"
marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)
total = marks1 + marks2 + marks3
print("Total Marks:", total)

# Question 51 — Type Casting Output
a = "50"
b = int(a)
print(a)
print(b)
print(type(a))
print(type(b))

# Question 52 — Float to Integer
number = 99.99
result = int(number)
print(number)
print(result)
# int() removes the decimal portion; it does not round the number.

# Question 53 — Arithmetic Output
a = 12
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# Question 54 — Parentheses Challenge
print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 / 5 + 3)
print(20 / (5 + 3))
# Parentheses force the expression inside them to be calculated first.

# Question 55 — Digit Challenge
number = 684
a = number % 10
b = number // 10
c = b % 10
d = number // 100
print(a)
print(c)
print(d)
# a = ones, c = tens, d = hundreds

# Question 56 — Debug the Student Program
student_name = "Ravi"
marks = "85"
total = int(marks) + 5
print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))

# Question 57 — Debug the Number Program
number = 746
ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100
print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)

# Question 58 — Debug the Discount Program
price = "2000"
discount = "15"
price = float(price)
discount = float(discount)
discount_amount = price * discount / 100
final_price = price - discount_amount
print("Discount:", discount_amount)
print("Final Price:", final_price)

# Question 59 — Complete Debugging Challenge
student_name = "Rahul"
marks1 = "85"
marks2 = "90"
marks3 = "78"
marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)
total = marks1 + marks2 + marks3
average = total / 3
print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))

# Question 60 — Final Challenge
# Part A — Number Analysis
number = 5836
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10
digit_sum = thousands + hundreds + tens + ones
reversed_number = ones * 1000 + tens * 100 + hundreds * 10 + thousands

print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)
print("Sum of Digits:", digit_sum)
print("Reversed Number:", reversed_number)

# Part B — Product Billing
price = "1250"
quantity = "4"
discount = "10"
price = int(price)
quantity = int(quantity)
discount = float(discount)
subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)
