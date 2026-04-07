# Write a programe that takes two number and print:
# Their sum,difference and product
# Whether the first number is greater then second 

num1= float(input ("Enter first number:"))
num2= float(input("Enter second number:" ))

sum_result =  num1+num2
difference= num1 - num2
product= num1 * num2
print("Sum:", sum_result)
print("difference:", difference)
print("Product", product)

if num1> num2:
    print("First number is greater than second")
elif num1< num2:
    print("Second number is greather than first")
else:
    print("Both number are equal")