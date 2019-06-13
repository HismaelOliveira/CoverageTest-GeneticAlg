def test_func(x,y,z,w):
    if x > y and x>z:
        print(x)
        if x < 2*y:
            print(2*y)
        else:
            print(3*z)

        if x> w:
            print(x)
        else:
            print(w*2)
    if y > x:
        print(y)

    if y>w:
        print(w)
    else:
        print(2*y)

    if x == z:
        print(z)
    if z>x:
        print(2*z)
    soma = x+y+z+w

    return soma
