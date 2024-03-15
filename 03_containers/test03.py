import copy
from collections import namedtuple

# List容器 操作
def test1():
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
def test2():
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
def test3():
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
def test4():
    someThing = "aaa"
    print(f'out method before: str="{someThing}"')
    addStr(someThing)
    print(f'out method after: str="{someThing}"')


def addElement(list):
    print(f'in method before: list="{list}"')
    list += ["后缀"]
    print(f'in method after: list="{list}"')


# 列表是可变的
def test5():
    list = ["1", "2", "3"]
    print(f'out method before: list="{list}"')
    addElement(list)
    print(f'out method after: list="{list}"')


# 元祖构建
def test6():
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


def test7():
    hw = getHW()
    print(hw, type(hw))
    # 自动解包
    width, height = getHW()
    print(width)
    print(height, type(height))


def test8():
    # 列表推导式
    res = [i * 100 for i in range(10) if i % 2 == 0]
    print(res)

    # 元祖没有推导式
    res_tuple = (i * 100 for i in range(10) if i % 2 == 0)
    print(res_tuple) # 返回了生成器
    res_tuple_b = tuple(res_tuple)
    print(res_tuple_b)


def test9():
    list = ["name",13,"des",True]
    print(list[2])

    userinfo = ("name",13,"des",True)
    print(userinfo[3])

def test10():
    my_tuple = ("aaa","bbb","ccc",100,200)
    print(my_tuple[0])
    print(my_tuple[2])

    # 具名元祖
    names = namedtuple('names', 'nameA,nameB,nameC,width,height')
    my_tuple_2 = names("aaa","bbb","ccc",100,200)
    my_tuple_3 = names(nameA="1212",nameB="sdfsdfsdf",width=1,height=222,nameC=1)
    print(my_tuple_2.width)
    print(my_tuple_2.nameB)
    print(my_tuple_3.width)
    print(my_tuple_3.nameB)




######################################## 字典 ########################################
# 字典基操
def test11():
    movie = {"name":"摔跤吧爸爸","type":"movie","year":2222}
    print(movie['name'])
    print(type(movie['year']))
    print(movie['year'])

    movie['type'] = "剧情片"
    print(movie)

    # 字典遍历
    for key in movie:
        print(key,":",movie[key])

    for k,v in movie.items():
        print(k,",,,,,",v)

    # key 不存在异常
    # print(movie['ssssss'])
    if 'ssssss' in movie:
        print("key exist")
    else:
        print("key not exist")

    try:
        print(movie['ssssss'])
    except KeyError:
        print("key error")

    print(movie.get("ssssss","sssss不存在返回默认值"))



def test12():
    movie = {"name": "摔跤吧爸爸", "type": "movie", "year": 2222,"actor":["amierhan","huangchnb","others"]}
    movie['actor'].append("append some thing")
    print(movie)

    # 不存在的key
    # movie['comments'].append("good good good")
    movie.setdefault('comments',['first comment','第二条评价']).append("good good good")
    print(movie)

    # 正常删除key,需要捕获key不存在的异常
    try:
        del movie['sssssssssss']
    except KeyError:
        pass

    print(movie)


    # pop用于取出某个key的value
    # 在这里可以用来删除某个key，不用抛出异常的写法
    name_value = movie.pop("name", "something")
    print(name_value)
    print(movie)
    ssss = movie.pop("sssssss", "默认值")
    print(ssss)
    movie.pop("sssssss",None)

# 字典推导式
def test13():
    movie = {"name": "摔跤吧爸爸", "type": "movie", "year": 2222, "actor": ["amierhan", "huangchnb", "others"]}
    res = {key:value*10 for key,value in movie.items() if key == "year"}
    print(res)


######################################## 集合 ########################################
# 集合（无序，不重复）
def test14():
    coll = {"apple","banana","apple","orage","换","换","我"}
    print(coll)

    nums = [1,2,3,2,3]
    print(nums)
    nums2 = {1, 2, 3, 2, 3}
    print(nums2)

    # 集合推导式
    t = {n*10 for n in nums if n <=3}
    print(t)

    # 初始化集合另一种方式
    empty_set = set()
    empty_set.add("apple")
    empty_set.add("apple")
    empty_set.add("ssssss")
    print(empty_set)

    another_set = set(["apple","apple","a","b","b","c"])
    print(another_set)

    # 不可变集合
    notChange = frozenset(["apple","b"])
    # notChange.add("sdf")


# 集合运算
def test15():
    a = {'a','b','c','d','d',1,2}
    b = {'a','b','r','r',2}
    c = {'f'}
    # 交集
    print(a & b)
    print(a.intersection(b))

    # 并集
    print(a | b)
    print(a.union(b))

    # 差集 (前一个集合有 后一个集合没有的)
    print(a - b)
    print(a.difference(b))
    print(c - b)
    print(b - c)


# 可哈希性
# 集合只能放可哈希性对象
def test16():
    dict_a = {"a","b",('ffff',)}
    print(dict_a)
    dict_b = {"a","b",['a','b']} #报错 list列表 不可哈希
    print(dict_b)
    # 传染性 ： tuple里面放入可变的list，也会变的不可哈希

    # 所有的不可变内置类型，都是可哈希的，比如 str、int、tuple、frozenset 等
    # 所有的可变内置类型，都是不可哈希的，比如 dict、list 等
    # 对于不可变容器类型 (tuple, frozenset)，仅当它的所有成员都不可变时，它自身才是可哈希的
    # 用户定义的类型默认都是可哈希的


# 浅拷贝
def test17():
    #
    nums = [1,2,3,4,5,6]
    nums_copy = nums
    nums_copy[2] = 100
    print(nums)
    print(nums_copy)

    # copy方法浅拷贝对象,修改后 原来的值不会改变
    nums_copy_2 = copy.copy(nums)
    nums_copy_2[3] = 999
    print(nums_copy_2)
    print(nums)

    # 列表推导式产生的也是浅拷贝对象
    d1 = {'a':1,'b':2,'c':3}
    d2 = {k:v for k,v in d1.items()}
    d1['a'] = 111
    print(d1)
    print(d2)

    # 构造函数浅拷贝
    listme = ['a','b','c']
    listme_copy = list(listme)
    listme_copy[2] = 'sdddddddd'
    print(listme)
    print(listme_copy)

    # 切片产生的也是浅拷贝对象
    list_4 = ['wo','he','ni']
    list_4_cp2 = list_4[:] #['wo','he','ni']
    list_4_cp1 = list_4[:-1] #['wo','he']
    list_4_cp2[2] = "wowowowowow"
    print(list_4)
    print(list_4_cp2)

    #自带copy方法
    list_5 = ['xin','lian','xin']
    list_5_copy = list_5.copy()
    list_5_copy[2] = 'newxin'
    print(list_5)
    print(list_5_copy)


# 深拷贝
def test18():
    items = ['1','2',['a','v'],'my']
    # 浅拷贝后,只修改第一层的值,不会影响原来
    items_copy = items.copy()
    # items_copy[3] = 'mynew'
    # print(items)
    # print(items_copy)

    # 这种也不会影响原来
    # items_copy[2] = ['a','v','new','ssss']
    # print(items)
    # print(items_copy)

    # 这种会产生影响
    items_copy[2].append("newsomething")
    print(items)
    print(items_copy)
    print(id(items_copy[2]),id(items[2]))  # 是一个对象

    items_deep_cp = copy.deepcopy(items)
    print(id(items[2]),id(items_deep_cp[2])) # 不是一个对象了


# 生成器 目的在按需返回 不是一次性全部返回
def generateNum(max_num):
    for i in range(0,max_num):
        if i%2 == 0:
            yield i
# 生成器
def test19():
    num = generateNum(10)
    print(num)
    for i in generateNum(10):
        print(i)

    print(list(generateNum(10)))




if __name__ == '__main__':
    print("---main start---")
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    # test9()
    # test10()
    # test11()
    # test12()
    # test13()
    # test14()
    # test15()
    # test16()
    # test17()
    # test18()
    test19()