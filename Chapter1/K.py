#输出幸运数字
import random
name = input("请输入你的名字：")
lucky = 1
random.seed(7)
for c in name:
    lucky += ord(c)*random.randint(1,100) 
print("你的幸运数字是：{}".format(lucky%777))
 