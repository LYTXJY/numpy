#基本操作

import numpy as np
import sys, math, os

def test_0():


    def test_0_0():
        """
        数组的算术运算符会应用到元素级别.
        下面创建一个新数组并填充结果的示例
        """
        a = np.array([20, 30, 40, 50])
        b = np.arange(4)
        print("b : ", b)
        c = a - b
        print("c :", c)
        b = b ** 2 
        print("b :", b)

        d = 10 * np.sin(a)
        print("d :", d)

        e = a < 35
        print("e :", e)



    def test_0_1():
        """
        与许多矩阵语言不同,乘积运算 * 在 Numpy数组中按元素进行源算.
        矩阵乘积可以使用 @ 运算符 或 dot 函数方法执行
        """
        A = np.array([[1, 1],
                    [0, 1]])
        print('A : \n', A)
        B = np.array([[2, 0],
                    [3, 4]])
        print("B : \n", B)

        C = A * B   # Matrix elementwise operations
                    #矩阵的元素操作
                    #elementwise product (product 产品;乘积)
        print("C : \n", C)

        D = A @ B   #matrix product
        print('D : \n', D)

        E = A.dot(B)    # another matrix product
        print("E : \n", E)

    def test_0_2():

        a = np.ones((2,3), dtype=int)
        b = np.random.random((2,3))
        a *= 3
        print("a : \n", a)
        b += a
        print("b : \n", b)


    # a +=b #cast 投 ；b is not automatically converted to interger type
    # print("a : \n", a)


    
    def test_0_3():
        """
        当使用不同类型的数组进行操作时,结果数组的类型对应于更一般或更精准的数组(称为向上转换的行为)
        """
        a = np.ones(3, dtype=np.int32)
        print("a  \n",a)
        b = np.linspace(0, math.pi, 3)
        # b = np.linspace(0, 5, 3)
        print("b : \n", b)
        print("b.dtype.name :", b.dtype.name)
        
        c = a + b
        print("c : \n", c)
        print('c.dtype.name :', c.dtype.name)

        d = np.exp(c  * 1)
        #牢记, numpy中的 乘法  * , 一定是对于元素级别的
        #如果想要进行矩阵级别的 操作 ,必须使用dot 与 @
        print("d : \n", d)
        print("d.dtype.name : ", d.dtype.name)

    # test_0_3()

    def test_0_4():
        """
        一元操作, 例如计算数组中所有元素的总和,都是作为ndarray类的方法实现的
        """
        # a = np.random.randint(0,10,(2,3))
        a = np.random.random((2,3))
        print("a : \n", a)

        b = a.sum()
        print("b : \n", b)

        c = a.min()
        print("c : \n", c)

        d = a.max()
        print("d : \n", d)

    
    # test_0_4()

    def test_0_5():
        """
        默认情况下,这些操作适用于数组,就像它是一个数字列表一样,无论其形状如何.
        但是通过指定 axis 参数, 可以沿数组的指定轴应用操作
        """
        b = np.arange(12).reshape(3, 4)
        print("b : \n", b)
        print("b.ndim : ", b.ndim)
        # print("b.axis : ", b.axis)


        b1 = b.sum(axis = 0) #sum of each column : 每列相加
        print("b1 : \n", b1)

        c = b.sum()
        print("c : \n", c)

        # d = b.sum(axis=1)
        # print("d : \n", d)

        d = b.min(axis =1)
        print("d : \n", d)

        e = b.cumsum(axis = 1)
        print("e : \n", e)




    # test_0_5()

    def test_0_6():
        """
        通函数
        数学函数:sin,cos,exp.这些在numpy中称为通函数(ufunc)
        在numpy中,这些函数在数组上按元素进行运算,产生一个数组作为输出

        """
        B = np.arange(3)
        print("B.dtype : ", B.dtype)
        print("B : \n", B )
        C = np.exp(B)
        print("C.dtype : ", C.dtype)
        print("C : \n", C)  #按元素进行运算

        D = np.add(B, C)
        print("D : \n", D)

        # B +=C
        # print("E : \n", B)
        #只有 += 时对参数的类型具有严格的限制,需要保持精度格式一致
        

    


    test_0_6()
    

if __name__ == "__main__":
    
    test_0()