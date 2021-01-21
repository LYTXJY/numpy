import numpy as np


def test_0():


    def test_0_1():
        """
        索引,切片和迭代

        一维的数组可以进行索引,切片和迭代操作.就像列表和其它python序列类型一样
        """
        
        a = np.arange(10)**3
        print("a ", a)
        print("a[2]", a[2])
        print("a[2:5] ", a[2:5])
        print("a[:6:2]", a[:6:2]) #from start to position 6 
        print("a[0:6:2] ", a[0:6:2]) #exclusive, set every 2nd element to -1000
        a[:6:2] = -1000
        print("a[:6:2] = -1000 : ", a)

        print("a[::-1]", a[::-1])

        for i in a:
            print(i ** (1/3.0))


    # test_0_1()

    def test_0_2():
        """
        多维的数组每个轴可以有一个索引.这些索引以逗号分隔的元祖给出:
        """
        def f(x, y):
            
            return 10 * x + y

        b = np.fromfunction(f, (5,4), dtype = int)
        print("b : \n", b)

        # print(help(np.fromfunction))
        #numpy.fromfunction(function, shape, **kwargs)
        #关键在于第二个参数shape,(N,)定义了fromfunction的输出数据形式


        #从上面的测试可以看出，shape()定义了输出矩阵的大小。
        # 如shape(5,4)，则x参数是5行1列行列式[0,1,2,3,4]. y参数1行4列行列式[0,1,2,3]. 
        #  将x,y带人func函数计算，最后结果的每个元素是根据func 函数来计算得出。

        print("b[2,3] : ", b[2, 3])
        print("b[0 : 5, 1]", b[0 : 5, 1]) #each row in the second colume of b(每一行第二列)
        print("b[:, 1]", b[:, 1])#equivalent to the previous example

        print("b[1:3, :] \n", b[1:3, :])

        """
        当提供的索引少于轴的数量时,缺失的索引1被认为是完整的切片


        ...

        numpy的 三个点 ... 表示产生完整索引元祖所需的冒号
        
        假设x的维度为5
        x[1, 2, ...] 相当于 x[1,2, :, :, :]
        x[..., 3] 相当于 x[:, :, :, :, 3]
        x[4, ..., 5, :] 相当于 x[4, :, :, 5, :]
        """

        print("b[1]", b[-1])

        c = np.array([[[0, 1, 2],
                        [10, 12, 13]],
                        [[100, 101, 102],
                        [110, 112, 113]]
                        ])
        print("c.shape : ", c.shape)
        print('c : \n', c)
        print("c[1, ...] : \n", c[1, ...])
        print("c[..., 2] : \n", c[..., 2])


        """
        对多维数组进行迭代(iterating)是相对于第一个轴完成的:
        """
        for row in b :
            print("b row", row)

        """
        但是,如果想要对数组中的每个元素执行操作,可以使用flat属性,该属性是数组的所有元素的迭代器
        """
        for element in b.flat:
            print("b.flat element :", element)

    # test_0_2()

    def test_0_3():
        """
        形状操纵
        """
        
        """
        改变数组的形状
        一个数组的形状是由每个轴的元素数量决定的
        """
        
        a = np.array(1 * np.random.random((3,4)))# np.random.random(shape), 浮点范围(0~1)
        a1 = np.floor(a)
        print("a : \n", a)
        print("a1 : \n", a1)

        

    
    test_0_3()



if __name__ == "__main__":
    test_0()