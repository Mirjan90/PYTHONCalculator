#Basic Calculator

x = int(input("First number: "))
y = int(input("Second number: "))

operation = input("What kind of operation would you like to do with numbers (+ , - , / , *): ")

if operation == "+":
    print(x + y)

elif operation == "-":
    print(x - y)

elif operation == "/":
    print(x / y)

elif operation == "*":
    print(x * y)

else:
    print("Write correct operation!")