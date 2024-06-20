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
