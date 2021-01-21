"""

numpy中的维度称为轴

np.array 不同于 array.array
    ndarray.ndim : 数组的轴(维度)的个数
    ndarray.shape :  数组的维度
    ndarray.size :  数组元素的总数
    ndarray.dtype :  一个描述数组中元素类型的对象
    ndarray.itemsize :  数组中每个元素的字节大小
    ndarray.data : 该缓冲区包括数组的实际元素









"""

import numpy as np
import math
import sys

def test_1():
    """
    一个例子
    """
    a = np.arange(15).reshape(3, 5)
    print("a.shape :", a.shape)
    print("a.ndim :", a.ndim)
    print("a.dtype.name :", a.dtype.name)
    print("a.itemsize :", a.itemsize)
    print("a.size :", a.size)
    print("type(a) :", type(a))

    b = np.array([6, 7, 8])
    print("type(b)", type(b))


def test_2():
    """
    数组创建
    """
    a = np.array([2,3,4])
    print("a : ", a)
    print("a.dtype :", a.dtype)
    b = np.array([1.2, 3.5, 5.1])
    print("b.dtype : ", b.dtype)


    #常见错误,调用array的时候传入多个数字参数
    #而不是提供单个数字的列表类型作为参数

    # a = np.array(1, 2,2 ,3 )
    a1 = np.array([1, 232, 2323, 32])
    # print(a) #ValueError: only 2 non-keyword arguments accepted
    print(a1)

    
    #序列的序列  转换 二维数组
    #序列的序列的序列   转换  三维数组
    b1 = np.array([(1.5, 2, 3), (4, 5, 6)])
    print("b1 :", b1)


    #创建数组时,显式指定数组的类型
    c = np.array([ [1,2], [3, 4] ], dtype= complex)
    print("c : ", c)



    #通常数组的元素最初是未知的,但它的大小是已知的.
    #因此,numpy提供了几个函数来创建具有初始占位符内容的数组
    #这就减少了数组增长的必要,因为数组增长的操作花费很大


    #zeros : 零充

    #ones  : 全1

    #empty  : 初始内容随机, dtype是float64

    d = np.zeros((3, 4)) 
    print("d : \n", d)
    d1 = np.ones((2,3,4), dtype = np.int16)
    print("d1 : \n", d1)

    d2 = np.empty((2,3))
    print("d2 : \n", d2)

    #为了创建数字组成的数组,numpy提供一个类似于range的函数,即arrange,该函数返回数组而不是列表

    e = np.arange(10, 30, 5)
    print("e : ", e)
    e1 = np.arange(0, 2, 0.3)
    print("e1 : ", e1)

    f = np.linspace(0, 2, 9)
    print("f : ", f)

    x = np.linspace(0, 2*math.pi, 100)
    f1 = np.sin(x)
    print("f1 : \n", f1)



def test_3():
    """
    打印数组
    
    1.最后一个轴从左到右打印
    2.倒数第二个从上到下打印
    3.其余部分也从上到下打印,每个切片用空行分割

    将一维数组打印为行
    将二维数据打印为矩阵
    将三维数据打印为矩数组表
    """
    a = np.arange(6)
    print("a : \n", a)

    b = np.arange(12).reshape(4, 3)
    print("b : \n", b)

    c = np.arange(24).reshape(2, 3, 4)
    print("c : \n", c)

    d = np.arange(10000)
    print("d: \n", d)

    #太大的数组,仅打印角点, numpy会自动跳过中心部分
    e = np.arange(10000).reshape(100, 100)
    print("e : \n", e)

    #可以改变打印选项,强制输出所有元素
    # np.set_printoptions(threshold = sys.maxsize)
    np.set_printoptions(threshold=sys.maxsize)
    print("e : \n", e)




if __name__ == "__main__":
    # test_1()
    # test_2()
    test_3()
