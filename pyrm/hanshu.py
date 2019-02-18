def hello(name):
    print(f'Hello, {name}!')

# hello('Amy')


# 强制关键字参数
def recv(maxsize, *, block):
    pass

# recv(1024, True)    # 报错


# 变长关键字参数 **
def run(a, b=1, **kwargs):
    print(kwargs)

# run(1)
# run(1, b=2)
# run(1, c=3)


def run(name):
    s = f'{name}'
    for x in range(5):
        if x == 3:
            return
    print(s)


run('Test')


