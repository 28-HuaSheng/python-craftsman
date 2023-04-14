# 读取文件
def fun1():
    with open('hello.txt', 'r') as fp:
        print(fp.read())


# with open('hello.txt', 'r', encoding='gbk') as fp:
#     print(fp.read())

# 二进制模式读取文件
def fun2():
    with open('hello.txt', 'rb') as fp:
        print(fp.read())


# 写文件
def fun3():
    with open('output.txt', 'w', encoding='gbk') as fp:
        fp.write('你好，中国')
        # fp.write('你好，中国'.encode('utf-8'))


def upper_s(s):
    """把输入字符串里的所有 "s" 都转为大写"""
    return s.replace('s', 'S')


# bin_obj = b'super sunflowers.'
# str_obj = bin_obj.decode('utf-8')
# print(upper_s(str_obj))

def fun4():
    with open('output.txt', 'wb') as fp:
        str_obj = upper_s('super sunflowers.')
        bin_obj = str_obj.encode('utf-8')
        fp.write(bin_obj)


# 写文件/ 字符或字节都可以写入
def fun5():
    with open('output.txt', 'wb') as fp:
        str = "hahahasdsssssss,大王叫我来巡山"
        strUppser = upper_s(str)
        fp.write(strUppser.encode('utf-8'))

# 读取文件/ 字节可以解码 字符直接读
def fun6():
    with open('output.txt', 'rb') as stream:
         print(stream.read())
         # print(stream.read().decode('utf-8'))


if __name__ == '__main__':
    # fun2()
    # fun4()
    # fun5()
    fun6()
