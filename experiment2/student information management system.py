employees = []

def add_employees():
    emp_id = input("请输入员工工号：")
    emp_name = input("请输入员工姓名：")
    emp_sex = input("请输入员工性别：")
    emp_age = input("请输入员工年龄：")
    emp_salary= input("请输入员工工资：")

    for emp in employees:
        if emp['工号'] == emp_id:
            print("员工工号已经存在")
            return


    employees.append({
        "工号":emp_id,
        "姓名":emp_name,
        "性别":emp_sex,
        "年龄":emp_age,
        "工资":float(emp_salary),
    })
    print("员工添加成功！")


def modify_employees():
    emp_id = input("请输入要修改的员工的工号：")
    for emp in employees:
        if emp["工号"] == emp_id:
            new_emp_id = input("请输入员工工号：")
            new_emp_name = input("请输入员工姓名：")
            new_emp_sex = input("请输入员工性别：")
            new_emp_age = input("请输入员工年龄：")
            new_emp_salary = input("请输入员工工资：")
            emp["工号"]=new_emp_id
            emp["姓名"]=new_emp_name
            emp["性别"]=new_emp_sex
            emp["年龄"]=new_emp_age
            emp["工资"]=new_emp_salary
            print("修改成功！")
            return
        print("未找到员工工号！")


def display_employees():
    if not employees:
        print("当前没有员工信息！")
    else:
        print("所有员工信息如下：")
        for emp in employees:
            print(f"工号：{emp['工号']}，姓名：{emp['姓名']}，性别：{emp['性别']}，年龄：{emp['年龄']}，工资：{emp['工资']}")

def delete_employees():
    emp_id = input("请输入需要删除的员工工号：")
    for emp in employees:
        if emp['工号'] == emp_id:
            employees.remove(emp)
            print("员工删除成功！")
            return
    print("未找到该员工，请检查工号！")


def statistics():
    if not employees:
        print("当前没有员工信息！")
    else:
        # 确保所有工资都是 float 类型
        for emp in employees:
            if not isinstance(emp['工资'], (int, float)):
                try:
                    emp['工资'] = float(emp['工资'])
                except ValueError:
                    print(f"警告：员工 {emp['工号']} 的工资数据无效，已设置为 0.0")
                    emp['工资'] = 0.0

        total_salary = sum(emp['工资'] for emp in employees)
        avg_salary = total_salary / len(employees)
        max_salary = max(emp['工资'] for emp in employees)
        min_salary = min(emp['工资'] for emp in employees)

        print("\n统计信息如下：")
        print(f"平均工资：{avg_salary:.2f}")
        print(f"最高工资：{max_salary:.2f}")
        print(f"最低工资：{min_salary:.2f}")

def main_menu():
    while True:
        print("== == = 员工管理系统 == == = ")
        print("*1.新增员工")
        print("*2.修改员工")
        print("*3.删除员工")
        print("*4.显示所有")
        print("*5.统计信息")
        print("*6.退出")

        choice = input("请输入功能选项：").strip()

        if choice == '1':
            add_employees()
        elif choice == '2':
            modify_employees()
        elif choice == '3':
            delete_employees()
        elif choice == '4':
            display_employees()
        elif choice == '5':
            statistics()
        elif choice == '6':
            print("退出系统，感谢使用！")
            break
        else:
            print("无效选项，请重新输入！")


# 启动程序
if __name__ == "__main__":
    main_menu()