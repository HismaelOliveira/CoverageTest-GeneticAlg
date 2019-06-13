def test_func(x,y,z,w):

    if x>y:
        if z > 0:
            test_func((x-z),y,z,w)
    else:
        if z > w:
            if y > 0:
                test_func(x,y,(z-y),w)
