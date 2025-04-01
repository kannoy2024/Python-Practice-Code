def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    number = input("请输入一个正整数: ")
    try:
        number = int(number)  # 将输入转换为整数
        if is_prime(number):
            print(f"{number}是质数")
        else:
            print(f"{number}不是质数")
    except ValueError:
        print("输入无效，请输入一个正整数！")
main()