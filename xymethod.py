def random_x_y(a, b):
    import random
    # if a < b:
    #     a, b = b, a
    list_x_y = []
    for _ in range(2):
        list_x_y.append(random.randint(a, b))
    return list_x_y[0], list_x_y[1]