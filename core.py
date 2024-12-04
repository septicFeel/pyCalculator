out = 0

def calculator():
    
    num1 = float(input("\nPlease insert the first number: "))
    num2 = float(input("\nPlease insert the second number: "))
    operation = input("\nPlease select the wanted operation (+, -, *, /): ")
    result = 0
    
    match operation:
        case "+":
            result = num1 + num2
            print ("\nThe sum is: {}".format(result))
        case "-":
            result = num1 - num2
            print ("\nThe result of the subtraction is: {}".format(result))
        case "*":
            result = num1 * num2
            print ("\nThe result of the multiplication is: {}".format(result))
        case "+":
            if num2 != 0:
                result = num1 / num2
                print ("\nThe result of the division is: {}".format(result))
        case _:
            out = 1
            print ("\nNot a valid operation.")

while out != 1:
    calculator()