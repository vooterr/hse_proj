a = int(input("Введите целое число"))
b = int(input("Введите второе целое число"))
print("This is master branch")

c = int(input("Введите третье целое число"))
d = a + b
op = input("Введите +-*/")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
else:
    print(a / b)
print("end")