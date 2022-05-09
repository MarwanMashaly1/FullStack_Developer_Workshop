num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
if num2 > 0:
    div = num1/num2
power = num1**num2

print("addition = " + str(add))
print("substraction = " + str(sub))
print("multiplication = " + str(mul))
print("division = " + str(div))
print("power = " + str(power))