class Fib:
    def __init__(self, max):
        self.a = 0
        self.b = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


# f = Fib(100)
# for i in f:
#     print(i)

print(list(Fib(100)))
