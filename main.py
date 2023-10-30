import calculator


first_num = int(input("Enter the First Number: "))
second_num = int(input("Enter the Second Number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")


if operation == "add":
    calculator.add(num1=first_num, num2=second_num)

elif operation == "subtract":
    calculator.subtract(num1=first_num, num2=second_num)
  
elif operation == "multiply":
    calculator.multiply(num1=first_num, num2=second_num)
    
elif operation == "divide":
    calculator.divide(num1=first_num, num2=second_num)
 
else:
    print("Sorry, I do not understand your request.")
