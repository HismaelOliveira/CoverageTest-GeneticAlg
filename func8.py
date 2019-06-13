def test_func(x,y,z,w):

    if w > 0:
        if x < y:
            while x < y:
                x = x+w

            if x == y:
                pass
        elif x > y:
            while x > y:
                y = y+w
            if x == y:
                pass
        else:
            z = x
    elif z>0:
        if x < y:
            while x < y:
                x = x+z

            if x == y:
                pass
        elif x > y:
            while x > y:
                y = y+z
            if x == y:
                pass
        else:
            w = x        
