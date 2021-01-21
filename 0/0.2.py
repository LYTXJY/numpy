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
        
        a = np.array(10 * np.random.random((3,4)))# np.random.random(shape), 浮点范围(0~1)
        a1 = np.floor(a)#np.floor()返回不大于输入参数的最大整数。（向下取整）
        print("a : \n", a)
        print("a1 : \n", a1)
        print("a.shape", a.shape)

        """
        可以使用各种命令更改数组的形状.
        以下三个命令都返回一个修改后的数组,但不会更改原始数组
        """  
        a1.ravel()#returns the array, flattened
        print("a1.ravel not carry \n", a1)
        print("a1.ravel \n", a1.ravel())

        print("a1.reshape(6, 2) : \n", a1.reshape(6,2))#returns the array with a modified shape

        print("a1.T : \n", a1.T)#returns the array, transposed

        print("a1.shape :  ", a1.shape)
        print("a1.T.shape :  ", a1.T.shape)

        """
        由ravel 产生的数组中元素的顺序通常是"C风格",也就是说,最右边的索引变化最快,因此[0,0]之后的元素
        是[0,1].如果将数组重新整形为其它形状,则改数组将被视为c风格.numpy通常创建按此顺序存粗的数组
        因此reval通常不需要复制其它参数,但如果数组是通过获取另一个数组的切片或者使用不常见的选项创建的
        则可能需要复制它.还可以使用可选参数指示函数ravel()和reshape(),以使用FORTRAN样式的数组,其中最左边的索引变化最快.

        该reshape函数返回带有修改形状的参数,而该ndarray.resize方法会修改数组本身
        """

        print("a1 : \n", a1)
        print("a1.resize((2,6)) : \n", np.resize(a1, (2,6)))
        # print("a1.resize((2,6)) : \n", a1.resize((2,6)))
        #官网给的是a1.resize((2,6))

        #在reshape操作中将size指定为-1,则会自动计算其它的size大小

        print("a1.reshape(3,-1) : \n", a1.reshape(3, -1))

    
    # test_0_3()


    def test_0_4():
        """
        将不同数组堆叠在一起

        ValueError: all the input array dimensions except for the concatenation axis must match exactly
        要求dimentions一致
        """
        a = np.floor(10 * np.random.random((2, 2)))
        print("a : \n", a)

        b = np.floor(10 * np.random.random((2, 2)))
        print("b : \n", b)

        c = np.vstack((a, b))
        print("c vstack : \n", c)

        d = np.hstack((a, b))
        print("d hstack : \n", d)
        

    # test_0_4()


    def test_0_5():
        """
        该函数将column_stack 1D数组作为列堆叠到2D数组中.
        它仅相当于 hstack 2D数组
        """

        a = np.array(10 * np.random.random((2,2)))
        a = np.floor(a)
        b = np.array(10 * np.random.random((2,2)))
        b = np.floor(b)

        from numpy import newaxis
        e = np.column_stack((a, b)) #with 2D arrays
        print("e np.column_stack((a, b)) : \n", e)

        a = np.array([4., 2.]);print("a.shape={}, a.ndim={}".format(a.shape, a.ndim))
        b = np.array([3., 8.]);print("b.shape={}, b.ndim={}".format(b.shape, b.ndim))

        c = np.column_stack((a, b)) #returns a 2D array
        print("c np.column_stack((a, b)):\n", c)

        d = np.vstack((a, b))
        print("d vstack((a, b)) \n", d) # the result is different

        e = a[:, newaxis] #this allows to have a 2D columns vector
        print("e : \n", e)
        print("e=a[:, newaxis]  e.shape={}, e.ndim={}".format(e.shape, e.ndim))

        f = np.column_stack((a[:, newaxis], b[:, newaxis]))
        print("f : \n", f)


        g = np.hstack((a[:,newaxis], b[:, newaxis]))#the result is the same
        print("g : \n", g)
    

        """
        另一方面,该函数(np.column) ma.row_stack 等效vstack 于任何输入数组
        通常,对于具有两个以上维度的数组,hstack沿其第二轴堆叠, vstack沿其第一轴堆叠

        注意
        在复杂的情况下,r_ 和 c_ 于通过沿一个轴堆叠数字来创建数组很有用.
        他们允许使用范围操作符(":")
        """
        k = np.r_[1:4, 0, 4]
        print("k", k)
        

    
    # test_0_5()


    def test_0_6():
        """
        np.r_       r row 行
        np.c_       c column 列
        """
        a = np.array([[1,2,3], [7,8,9]]);print("a :\n", a)
        b = np.array([[4,5,6], [1,2,3]]);print("b : \n", b)

        c = np.r_[a, b];print("c np.r_[a, b] :\n", c)

        d = np.array([7,8,9])
        e = np.array([1, 2, 3])

        f = np.c_[d,e]
        print("f :\n", f)

        j = np.r_[d, e]
        print("j :\n", j)

    # test_0_6()

    def test_0_7():

        """

        将一个数组拆分成几个较小的数组

        使用hsplit 可以沿数组的水平轴拆分数组, 方法是指定要返回的形状相等的数组的数量,
        或者指定一般改在其之后进行分割的列
        """

        a = np.floor( 10 *np.random.random((2, 12)))
        print("a : \n", a)

        b = np.hsplit(a, 3)#indices_or_sections 指标of部分 ；split a into 3
        print("b :\n", b)

        e = np.vsplit(a, 2)#indices_or_sections 指标of部分 ；split a into 2
        print("e :\n", e)

        f = np.hsplit(a, (3, 4))
        print("f : \n", f)





    test_0_7()



if __name__ == "__main__":
    test_0()