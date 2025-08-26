try:
    age=int(input("Enter the age: "))

except ValueError:
    print("You gave an invalid value.Please try again with a numerical value")
    age=int(input("Enter the age: "))

if age>=18:
    print(f"You can drive at this age--{age}")
else:
    print(f"You canNOT drive at this age--{age}")
