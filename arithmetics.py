def add(x,y):
    return x + y


def sub(x,y):
    return x - y


def mul(x,y):
    return x * y


def div(x,y):
    if y == 0:
        raise ValueError("Can't divided by zeros")

    return x // y