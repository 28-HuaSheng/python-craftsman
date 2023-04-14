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
    # for number in numbers:
    #     if number % 2 == 1:
    #         continue
    #     result.append(number * 100)
    # print(result)

    # 使用推导





if __name__ == '__main__':
    print("---main start---")
    # fun1()
    # fun2()
    fun3()
