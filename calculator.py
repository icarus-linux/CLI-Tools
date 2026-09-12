print("--- CLI Calculator ---")

# Numbers
value1 = int(input("Enter first value: "))
value2 = int(input("Enter second value: "))

# Opperation
opperation = input("Choose opperation +, -, / or * : ")


if(opperation == "+"):
    print("the value is :" + value1 + value2)
if(opperation == "-"):
    print("the value is : " + value1 - value2)
if(opperation == "/"):
    print("the value is : " + value1 / value2)
if(opperation == "*"):
    print("the vlaue is : " + value1 * value2)
else:
    print("This is an invalid opperation")
 




