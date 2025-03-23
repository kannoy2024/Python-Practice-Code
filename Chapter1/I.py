sum,tmp = 0,1
for i in range(1,11):
    tmp *= i
    sum += tmp
    print("运行结果是：{}".format(sum))
    # 求1!+2!+3!+4!+5!+6!+7!+8!+9!+10! 的结果 