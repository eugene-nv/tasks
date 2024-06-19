lst = [('+', 1, 1), ('*', 2, 3)]


def calculate_function(data):
    def action(i):
        if i[0] == "+":
            return i[1] + i[2]
        elif i[0] == "-":
            return i[1] - i[2]
        elif i[0] == "*":
            return i[1] * i[2]
        elif i[0] == "/":
            return i[1] / i[2]
        elif i[0] == "**":
            return i[1] ** i[2]

    return list(map(action, data))


print(calculate_function(lst))
