#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as computation
    a = 10
    b = 5

    total = computation.add(a, b)
    diff = computation.sub(a, b)
    product = computation.mul(a, b)
    qoutient = computation.div(a, b)

    print("{} + {} = {}".format(a, b, total))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, product))
    print("{} / {} = {}".format(a, b, qoutient))
