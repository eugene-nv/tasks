import random


def cache_function():
    count = 0
    value = random.randint(1, 111)

    def inner():
        nonlocal count, value

        if count != 3:
            count += 1
            return value

        else:
            count = 1
            value = random.randint(1, 111)
            return value

    return inner


