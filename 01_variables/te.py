
def test1():
    author, reader = 'piglei', 'raymond'
    author, reader = reader, author
    print(author)


def test2():
    print("test2")


def test3():
    usernames = ["bobo","xiuxiu"]
    usernameA = usernames
    print(usernameA)
    firstName,secondName = usernames
    print(firstName)
    print(secondName)

# 变量解包
def test4():
    arr = [1,["bobo","xiuxiu"]]
    arrA,(arrB,arrC) = arr
    print(arrA)
    print(arrB)
    print(arrC)


# 动态解包
def test5():
    arr = ["bobo","banana","apple","orage","dsfsdfs","xiuxiu"]
    nameA,*fruit,nameB = arr
    print(nameB)
    print(fruit)


# 常规切片赋值 和 上面的动态解包比较 不够直观
def test6():
    arr = ["bobo","banana","apple",1,"xiuxiu"]
    boboname = arr[0]
    print(boboname)
    xiuxiuname = arr[-1]
    print(xiuxiuname)

    fruit = arr[1:-1] #左包含右不包含
    print(fruit)


# 解包在循环中
def test7():
    for username,age in [("boob",18),("xiuixiu",18),("duoduo",10)]:
        print(username)
        print(age)


if __name__ == '__main__':
   # test1()
   # test2()
   # test3()
   # test4()
   # test5()
   # test6()
   test7()