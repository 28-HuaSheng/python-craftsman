from decimal import Decimal


# 整型/浮点互相转换
def fun1():
    temp = 1000
    floats = 222.222
    print(temp, floats)
    print(float(temp), int(floats))


# 浮点计算 (注意浮点陷阱)
def fun2():
    tmp = 0.1
    tmp2 = 0.2
    print(tmp + tmp2)

    tmp3 = Decimal(0.1) + Decimal(0.2)
    tmp4 = Decimal("0.1") + Decimal("0.2")
    print(tmp3)
    print(tmp4)


# 布尔类型也是数字
def fun3():
    var1 = True
    var2 = False
    print(int(var1), int(var2))


# 获取奇偶数量
def fun4():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    print(count)


# 根据True=1 False=0特性获取奇偶数量
def fun5():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = sum(i % 2 == 0 for i in numbers)
    print(count)


# 字符串
def fun6():
    str = "hello, world"
    for i in str:
        print(i)

    str2 = str[1:3]
    print(str2)

    str3 = str[::-1]
    print(str3)

    print(reversed(str))
    str4 = "".join(reversed(str))  # join--连接任意数量的字符串，比如用 ""连接一系列字符, " ".join(数组)表示用空格把数组所有元素连接成一个字符串
    print(str4)


# 字符串格式
def fun7():
    username, age = "huangchunbo", 18
    # c语言格式化
    print("this name is:%s,and age is:%d" % (username, age))

    # 另一种格式化
    print("this name is:{},and age is:{:d}".format(username, age))

    # 另一种格式化
    print(f"this name is:{username},and age is:{age:d}")


# 字符向右移动20
def fun8():
    username = "huang"
    print("{:>20}".format(username))
    print(f"{username:>30}")
    print(f"{username:>40}")


# 还是格式化
def fun9():
    nameA, nameB, nameC = "aaaaaa", "bbbbb", "cccccc"
    print("{0}------{1}-------{2}------{0}".format(nameA, nameB, nameC))
    print(f"{nameA}------{nameC}-------{nameC}------{nameC}")


def fun10():
    words = ["this is some word:"]
    for i in range(10):
        words.append(f"{i + 1}")
    print('\n'.join(words))


# 字符串一些方法
def fun11():
    word = "hello, world , i am ..."
    numberStr = "123"
    print(numberStr.isdigit())
    print(word.isdigit())
    print(f"split : {word.split(' ')}")
    print(f"partition : {word.partition(' ')}")
    print(f"partition : {word.partition('world')}")  # 通过给定分隔符把原字符分三段： 分隔符前/分隔符/分隔符后
    print("-------".join(word.split(" ")))


# translate 一次性替换多个符号
def fun12():
    word, name = "你好，我是刘某。我的标点等待替换。", "发发发，123，"
    word_table = word.maketrans('，。', ',.')
    name_table = name.maketrans('，', '!')
    new_word = word.translate(word_table)
    new_name = name.translate(name_table)
    print(new_word)
    print(new_name)


def fun13():
    # 一字节 = 8位 = xYY(16进两位刚好表示一个字节)
    str_str = "hello, 摩托"
    print(type(str_str))

    print(str_str.encode())

    # 证明默认是utf8编码
    print(str_str.encode() == str_str.encode('UTF-8'))

    str_byte = b'helllooooooo'
    print(type(str_byte))
    print(str_byte.decode())


def fun14():
    log_line = '"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"         47632'
    l = log_line.split()
    print(l)
    print(l[:-1])
    line_ = " ".join(l[:-1]), log_line[-1]
    print(line_)
    print(line_[0])
    print(line_[1])


def fun15():
    arr1 = ["ssssss", "ooooooo", "bbbbbb"]
    arr2 = ["我们", "花园"]
    print(arr1)
    join = " ".join(arr1), arr2[1]
    print(join)
    tet = "ssfsdfsdf", "sdfsfsdfsdfsdfsd"  # 这是一个tuple,不能进行改变内部值  TypeError: 'tuple' object does not support item assignment
    print(tet)
    tet[1] = "hahah"
    print(tet)


# 字符切割 从右往左
def fun16():
    str = "heew sdfsd,sdfds sdf sdf"
    print(str.split(' '))
    print(str.split(' ', maxsplit=1))  # 切割一次
    print(str.rsplit(' ', maxsplit=1))


if __name__ == '__main__':
    # fun1()
    # fun2()
    # fun3()
    # fun4()
    # fun5()
    # fun6()
    # fun7()
    # fun8()
    # fun9()
    # fun10()
    # fun11()
    # fun12()
    # fun13()
    #    fun14()
    fun15()
# fun16()
