#!/usr/bin/python3
import calculator_1

a = 10
b = 5

total = calculator_1.add(a, b)
diff = calculator_1.sub(a, b)
product = calculator_1.mul(a, b)
qoutient = calculator_1.div(a, b)

print("{} + {} = {}".format(a, b, total))
print("{} - {} = {}".format(a, b, diff))
print("{} * {} = {}".format(a, b, product))
print("{} / {} = {}".format(a, b, qoutient))
