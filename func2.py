def test_func(x,y,z,w):

    if x > y:
        for i in range(x):
            y = y+z
    else:
        for i in range(y):
            x = x+w

    if x > y:
        x = y
    if x < y:
        y = x
    else:
        x = z+w
        y = x
