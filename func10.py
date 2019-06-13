def test_func(x,y,z,w):
    if w>0:
        if z > 0:
            for s in range(w):
                x = y/2
                for i in range(z):
                    y = y+s
        else:
            x = y*z
    elif w > y:
        pass
