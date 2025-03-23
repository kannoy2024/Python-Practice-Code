#回声程序，将用户的输入原封不动的返回给用户
echo = input("这是一个回声程序，请输入：")
eval("'echo'")
print("请看，这是你输入的内容：{}".format(echo))