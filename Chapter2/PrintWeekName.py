weekstr="星期一星期二星期三星期四星期五星期六星期日"
weekid = eval(input("请输入星期几的数字(1-7)："))
pos =(weekid-1)*3
print(weekstr[pos:pos+3])#使用切片的方式输出字符串。每三个为一片