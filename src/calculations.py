def sum(*args):
    c=0
    for item in args:
        c+= item
    return c

def product(*args):
    p = 1
    for item in args:
        p*=item
    return p