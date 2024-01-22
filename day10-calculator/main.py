operations = {
    "+": "add",
    "-": "sub",
    "*": "multiply",
    "/": "divide"
}


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


first_number = int(input("What is your first number?: "))
result: int = 0
function_call = ""
program_continue = True
while program_continue:
    operation_user = input("Pick an operation: ")
    next_number = int(input("What's the next number?: "))
    for operation in operations:
        if operation_user == operation:
            function_call = operations[operation]

    if function_call == "add":
        result = add(first_number, next_number)
    elif function_call == "sub":
        result = sub(first_number, next_number)
    elif function_call == "multiply":
        result = multiply(first_number, next_number)
    elif function_call == "divide":
        result = divide(first_number, next_number)
    print(f"{first_number} {function_call} {next_number} = {result}")

    go_on = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")
    if go_on == "n":
        break
    elif go_on == "y":
        first_number = result



