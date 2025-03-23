diet = ['西红柿','黄瓜','花椰菜','虾仁','猪肉','牛肉']
for i in range(0,6):
    for y in range(0,6):
        if not i == y:
            print("{}炒{}".format(diet[i],diet[y]))
            #两次遍历相等就不输出，不相等就输出