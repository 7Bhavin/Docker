def add (num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

print("Please select an below options -\n"
			"1. Add\n"
			"2. Subtract\n"
			"3. Multiply\n"
			"4. Divide\n")
			
			
try:
	select = int(input("Select option form 1,2,3,4:"))

	if select not in [1,2,3,4]:
		print("Invalid option! Please enter a number between 1 and 4.")
	else:
		number1 = float(input("Enter First Number: "))
		number2 = float(input("Enter Second Number: "))

	if select == 1:
		print ( number1, "+", number2, "=", add(number1, number2))

	elif select == 2:
		print ( number1, "-", number2, "=", subtract(number1, number2))

	elif select == 3:
		print ( number1, "*", number2, "=", multiply(number1, number2))

	elif select == 4:
		print ( number1, "/", number2, "=", divide(number1, number2))

except ValueError:
    print("Invalid input! Please enter numeric values.")
