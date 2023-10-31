# Creating a calculator program using python 3
print(".................................................")
print("|                                               |")
print("|                                               |")
print("|           !!!!!Python Calculator!!!!          |")
print("|                                               |")
print("|                                               |")
print(".................................................")

# initializing the variable that will be used in the while loop condition
option = '0'

while option != '8':

    print("")
    print("Choose 1: To Add")
    print("Choose 2: To Subtract")
    print("Choose 3: To Divide")
    print("Choose 4: To Multiply")
    print("Choose 5: To Perform Floor Division")
    print("Choose 6: To find the Exponential Value")
    print("Choose 7: To find the Modulus")
    print("Choose 8: To Cancel")
    print("")

    # Accepting an input from the user

    option = input("What option do you choose: ")
    print("")

    # using an if-elif statement to test the conditions

    if option == '1':
        num1 = int(input("Please enter the first number: "))
        print("")
        num2 = int(input("Please enter the second number: "))
        print("")
        result = num1 + num2
        print(num1, " + ", num2, " = ", result)

    elif option == '2':
        num1 = int(input("Please enter the first number: "))
        print("")
        num2 = int(input("Please enter the second number: "))
        print("")
        result = num1 - num2
        print(num1, " - ", num2, " = ", result)

    elif option == '3':
        num1 = int(input("Please enter the first number: "))
        print("")
        num2 = int(input("Please enter the second number: "))
        print("")
        if num2 != 0:
            result = num1 / num2
            print(num1, " / ", num2, " = ", result)
        else:
            print("Error!!\nDivider should not be zero\nPlease put a value higher than zero.")

    elif option == '4':
        num1 = int(input("Please enter the first number: "))
        print("")
        num2 = int(input("Please enter the second number: "))
        print("")
        result = num1 * num2
        print(num1, " * ", num2, " = ", result)

    elif option == '5':
        num1 = int(input("Please enter the first number: "))
        print("")
        num2 = int(input("Please enter the second number: "))
        print("")
        if num2 != 0:
            result = num1 // num2
            print(num1, " // ", num2, " = ", result)
        else:
            print("Error!!\nDivider should not be zero\nPlease put a value higher than zero.")

    elif option == '6':

        num1 = int(input("Please enter the base number: "))
        print("")
        num2 = int(input("Please enter the exponent number: "))
        print("")
        result = num1 ** num2
        print(num1, " ** ", num2, " = ", result)

    elif option == '7':
        num1 = int(input("Please enter the first number: "))
        print("")
        num2 = int(input("Please enter the second number: "))
        print("")
        if num2 != 0:
            result = num1 % num2
            print(num1, " % ", num2, " = ", result)
        else:
            print("Error!!\nDivider should not be zero\nPlease put a value higher than zero.")

    elif option == '8':
        print("")
        print("You have successfully exited the program!!!")
        break

    else:
        print("")
        print("You have chosen an invalid option, Try Again!!!")


print("")
