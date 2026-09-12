print("--- CLI Calculator ---")

againUser = "yes"

while againUser == "yes":
    # Numbers
    value1 = int(input("Enter first value: "))
    value2 = int(input("Enter second value: "))

    # Opperation
    opperation = input("Choose opperation +, -, / or * : ")

    if(opperation == "+"):
        print("the value is :" + str(value1 + value2))
    elif(opperation == "-"):
        print("the value is : " + str(value1 - value2))
    elif(opperation == "/"):
        print("the value is : " + str(value1 / value2))
    elif(opperation == "*"):
        print("the vlaue is : " + str(value1 * value2))
    else:
        print("This is an invalid opperation")

    againUser = input("Calculate again? (yes/no): ")