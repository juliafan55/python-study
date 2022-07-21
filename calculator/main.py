# calculation functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    # storing the functions as values and key matches the symbol -> will be picked by user
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:

        # loop through operations list and print the key
        for symbol in operations:
            print(symbol)

        # operation symbol stores what user picked - will match from operations list
        operation_symbol = input("Pick an operation")

        num2 = float(input("What's the next number?: "))

        # access the function by entering operations list and grabbing the value (value matches the operation symnbol)
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # if the input matches "Y"
        if input("Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation") == "y":
            # set num1 as the answer from the calculation
            num1 = answer
        else:
            # ends calculation
            should_continue = False
            # call the function recursively to restart operations
            calculator()
