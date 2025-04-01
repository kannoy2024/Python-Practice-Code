# 获取用户输入的收入金额
income = float(input("请输入您的收入金额："))

# 起征点
threshold = 3500

# 计算应纳税所得额
taxable_income = income - threshold

# 如果应纳税所得额小于等于 0，则不需要缴纳税款
if taxable_income <= 0:
    tax = 0
else:
    # 初始化税款为 0
    tax = 0

    # 税率表，每个元素是一个元组 (应纳税所得额上限, 税率)
    tax_rates = [
        (1500, 0.03),
        (4500 - 1500, 0.1),
        (9000 - 4500, 0.2),
        (35000 - 9000, 0.25),
        (55000 - 35000, 0.3),
        (80000 - 55000, 0.35),
        (float('inf'), 0.45)
    ]

    # 遍历税率表，计算税款
    remaining_income = taxable_income
    for limit, rate in tax_rates:
        if remaining_income <= 0:
            break
        # 计算当前档位的应纳税所得额
        taxable_in_this_bracket = min(remaining_income, limit)
        # 计算当前档位的税款
        tax += taxable_in_this_bracket * rate
        # 更新剩余应纳税所得额
        remaining_income -= taxable_in_this_bracket

# 计算扣除所得税后的实际个人收入
actual_income = income - tax

# 输出结果
print(f"需要缴纳的个人所得税为：{tax:.2f} 元")
print(f"扣除所得税后的实际个人收入为：{actual_income:.2f} 元")