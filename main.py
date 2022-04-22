def incrementor(stride: int):
    def f(x: int):
        return stride + x
    return f

g = incrementor(1)
print(g(1))