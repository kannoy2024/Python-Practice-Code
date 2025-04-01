max=eval(input("请输入一个正整数作为Fibonacci数列的上限："))
a,b=1,1
count=0
while a<=max:
    print(a,end=", ")
    count+=1
    if count%4==0:
        print()
    a,b=b,a+b