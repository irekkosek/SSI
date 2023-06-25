def minkowski(x, y, p):
    return sum(abs(a-b)**p for a, b in zip(x, y))**(1/p)

def taxicab(x, y):
    return minkowski(x, y, 1)
def taxicab(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))
