operations = ["+", "-", "*", "/"]
operation = str(input("What operation do you want to do? The available operation are:\n+ for add\n- for substract\n* for multiply\n/ for divide\nEnter the operation you want to do here: "))

def add():
    sum = a + b

    print(f"The result is {sum}")

def substract():
    difference = a - b

    print(f"The result is {difference}")

def multiply():
    product = a * b
    print(f"The result is {product}")

def divide():
    dividednumber = a / b
    print(f"The result is: {dividednumber}")

if operation in operations:
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    
    try:
        a = float(a)
        b = float(b)
        
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            print("Invalid input. Please enter numeric values.")
        else:
            if operation == "+":
                add()
            elif operation == "-":
                substract()
            elif operation == "*":
                multiply()
            elif operation == "/":
                divide()
    except ValueError:
        print("Invalid input. Please enter numeric values.")
else:
    print("Invalid Operation!")


