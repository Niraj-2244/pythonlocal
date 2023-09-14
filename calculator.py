print("what do you want to do?")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

choice = input("Enter your choice: ")

num1 = float(input("Enter the Number 1 : "))
num2 = float(input("Enter the number 2 : "))

def addition(num1,num2):
    result = num1 + num2
    # print(result)
    print("{0} + {1} = {2}".format(num1,num2,result))

def subtraction(num1,num2):
    result = num1-num2
    print("{0} - {1} = {2}".format(num1.num2,result))


def multiplication(num1, num2):
    result = num1 * num2
    print("{0} * {1} = {2}".format(num1, num2, result))

def division(num1,num2):
    if num2 == 0.0:
        print("Cant Do divide by zero")
    else:
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1,num2,result))

if choice == '1':
    addition(num1,num2)


elif choice == '2 Subtraction':
    subtraction(num1, num2)


elif choice == '3':
    multiplication(num1, num2)


elif choice == '4':
    division(num1,num2)


else:
    print("Invalid choice")

