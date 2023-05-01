
print("Select an operation to perform")
print("1. ADD ")
print("2. SUBTRACT ")
print("3. MULTIPLY ")
print("4. DIVIDE ")

operation = int(input())                     # Taking input from user to choose which operation wants to perform


if operation == 1:
    num1=eval(input('Enter First Number :'))    # Using eval taking first number as input from user 
    num2=eval(input('Enter Second Number :'))    # Using eval taking second number as input from user   
    print('The Sum is ', num1 + num2) 
elif operation == 2:
    num1=eval(input('Enter First Number :'))     # Using eval taking first number as input from user
    num2=eval(input('Enter Second Number :'))     # Using eval taking second number as input from user
    print('The Substract is ', num1 - num2)
elif operation == 3:
    num1=eval(input('Enter First Number :'))      # Using eval taking first number as input from user
    num2=eval(input('Enter Second Number :'))      # Using eval taking second number as input from user
    print('The multiply is ', num1 * num2)
elif operation == 4:
    num1=eval(input('Enter First Number :'))      # Using eval taking first number as input from user
    num2=eval(input('Enter Second Number :'))      # Using eval taking second number as input from user
    print('The divide is ', num1 / num2)
else:
    print('Invalid Entry')
    