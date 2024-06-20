def add(x):
    def inner(y=None):
        if y is None:
            return x
        else:
            return add(x+y)
    return inner
