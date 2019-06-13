def test_func(x,y,z,w):
    for i in range(w):
        x = x+y
    if x > z:
        if w>0:
            while x > z:
                x = x-w
    if x == z:
        y = w
        z = y
    else:
        x = z
        z = w
