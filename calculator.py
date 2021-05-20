# Python Based Calculator By "Haseeb"

def add(num1 , num2):
    return num1 + num2

def substract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
    return num1 / num2

print("Pleas Select The Operation - \n" \
        "1. Add\n" \
        "2. Substract\n" \
        "3. Multiply\n" \
        "4. Divide")

select = int(input("Select Operation 1/2/3/4 :"))

num1 = int(input("Select First Number :"))
num2 = int(input("Select Second Number :"))

if select == 1:
    print(num1, "+", num2, "=" ,
                        add(num1 , num2))

elif select == 2:
    print(num1, "-", num2, "=" ,
                        substract(num1 , num2))

elif select == 3:
    print(num1, "X", num2, "=" ,
                        multiply(num1 , num2))

elif select == 4:
    print(num1, "/", num2, "=" ,
                        divide(num1 , num2))

else:
    print("Invalid Input")