

def construct(rows, cols):

    matrix = [[i for i in range(rows)]] * cols

    return matrix


print(construct(3, 3))