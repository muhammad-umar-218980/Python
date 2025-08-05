def calculator():


	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))

	operation = input("Enter operation (+, -, *, / , % , // , **): ")

	result = 0

	match operation:
		case '+':
			result = num1 + num2
		case '-':
			result = num1 - num2
		case '*':
			result = num1 * num2
		case '/':
			try: 
				result = num1 / num2
			except ZeroDivisionError:
				print("Cannot divide by zero")
		case '%':
			result = num1 % num2
		case '//':
			result = num1 // num2
		case '**':
			result = num1 ** num2
		case _:
			print('Invalid operation')

	if operation in ['+', '-', '*', '/', '%', '//', '**']:
		print(f"\n{num1} {operation} {num2} = {result}")
	else:
		print("Invalid operation")	


print('Welcome to the calculator!')

while True:
	calculator()
	cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
	if cont != 'yes':
		print("Exiting the calculator. Goodbye!")
		break


