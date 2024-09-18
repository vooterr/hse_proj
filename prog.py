a = int(input("Введите целое число"))
b = int(input("Введите второе целое число"))
op = input("Введите +-*/")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
else:
    print(a / b)