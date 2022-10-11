#:/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result: {:.1f}".format(c))
    return c
