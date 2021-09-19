import logging
def check(f):
    def inner(a, b, operator):
        if operator == '/':
            if a == 0 or b==0 :
                return logging.error("Error Zerodividion")
        return f(a, b, operator)
    return inner


@check
def calculate(x, y, ope):
    if ope == "+":
        return x + y
    elif ope == "-":
        return x - y
    elif ope == "*":
        return x * y
    elif ope == "/":
        return x / y

        