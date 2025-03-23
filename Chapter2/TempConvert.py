# TempConvert.py,温度转化
TempConvert = input("请输入带有符号的温度值，如23C或23F：")
if TempConvert[-1] in ['F','f']:
    C = (eval(TempConvert[:-1]) - 32)/1.8
    print("转换后的温度是，摄氏度{:.2f}C ".format(C))
elif TempConvert[-1] in ['C','c']:
    F = eval(TempConvert[ : -1 ] ) * 1.8 + 32
    print("转换后的温度是，\
                    华氏度{:.2f}F".format(F))#反斜杠用来切割代码
else:
    print("输入错误")
    '''
    这个是多行注释
    ''' 


    #eval()函数,将eval(TempConvert[:-1])转化成python的表达式运行