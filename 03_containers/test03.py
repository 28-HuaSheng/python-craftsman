# List容器 操作
def fun1():
    list_a = ["a", "b", "c", "d", "e"]
    list_b = list("abcdefghijklmn")
    print(list_a)
    print(list_b)

    print(list_b[2])
    print(list_b[:1])  # 打印1右边的，应该冒号放在1右侧，1:
    print(list_b[1:])
    print(list_b[:-1])
    print(list_b[:-2])

    # 删除
    del list_b[2]
    print(list_b)
    del list_b[2:]
    print(list_b)


# 遍历获取下标
def fun2():
    list_a = ["wo", "he", "ni", "xin", "lian"]

    # for tmp in list_a:
    #     print(tmp)

    # 带下标
    # for index, tmp in enumerate(list_a):
    #     print(index, tmp)

    # 指定index开始
    for index, tmp in enumerate(list_a, start=3):
        print(index, tmp)


# 列表推倒式
def fun3():
    result = []
    numbers = [1, 2, 3, 4, 5, 6]

    # 原来的做法
    for number in numbers:
        if number % 2 == 1:
            continue
        result.append(number * 100)
    print(result)

    # 使用推导
    results = [n * 100 for n in numbers if n % 2 == 0]
    print("results :")
    print(results)


# 可变性
# 可变：列表 字典 集合
# 不可变: 字符串 整数 浮点数 字节串 元祖
def addStr(str):
    print(f'in method before: str="{str}"')
    str += "后缀"
    print(f'in method after: str="{str}"')


# 字符串不可变
def fun4():
    someThing = "aaa"
    print(f'out method before: str="{someThing}"')
    addStr(someThing)
    print(f'out method after: str="{someThing}"')


def addElement(list):
    print(f'in method before: list="{list}"')
    list += ["后缀"]
    print(f'in method after: list="{list}"')


# 列表是可变的
def fun5():
    list = ["1", "2", "3"]
    print(f'out method before: list="{list}"')
    addElement(list)
    print(f'out method after: list="{list}"')


# 元祖构建
def fun6():
    yuan_a = ("a", "b", "c")
    yuan_b = "aa", "bb", "cc"
    yuan_c = tuple("abcdef")
    print(yuan_a)
    print(yuan_b)
    print(yuan_c)


def getHW():
    width = 100
    height = 10
    return width, height


def fun7():
    hw = getHW()
    print(hw, type(hw))
    # 自动解包
    width, height = getHW()
    print(width)
    print(height, type(height))


def fun8():
    # 列表推导式
    res = [i * 100 for i in range(10) if i % 2 == 0]
    print(res)

    # 元祖没有推导式
    res_tuple = (i * 100 for i in range(10) if i % 2 == 0)
    print(res_tuple) # 返回了生成器
    res_tuple_b = tuple(res_tuple)
    print(res_tuple_b)

def fun9():
    list = ["name",13,"des",True]
    print(list[2])

    userinfo = ("name",13,"des",True)
    print(userinfo[3])

if __name__ == '__main__':
    print("---main start---")
    # fun1()
    # fun2()
    # fun3()
    # fun4()
    # fun5()
    # fun6()
    # fun7()
    # fun8()
    fun9()