# 1，打印功能提示
print("="*50)
print("名片管理系统V1.0")
print("1：添加一个名片")
print("2：删除一个名片")
print("3：修改一个名片")
print("4：查询一个名片")
print("5: 显示系统内存储的所有名片信息")
print("6：退出系统")
print("="*50)

# 定义一个空的列表存放字典信息
cards = []

while True:
    # 2，用户输入功能标识
    num = int(input("请输入想要使用的功能前面的数字"))

    # 3，根据用户的输入执行相关的命令
    if num == 1:
        new_name = input("请输入姓名：")
        new_phone = input("请输入手机号：")
        new_address = input("请输入地址")
        # 定义一个字典用来存储名片
        business_card = dict()
        business_card["name"] = new_name
        business_card["phone"] = new_phone
        business_card["address"] = new_address
        # 将字典放到定义的列表中
        cards.append(business_card)
    elif num == 2:
        del_name = input("请输入你要删除的名字：")
        x = -1
        for card in cards:
            # 每迭代一个字典x+1,第一个字典位置加1后刚好为0
            x += 1
            if del_name == card["name"]:
                del cards[x]
                print("该名片已删除!")
    elif num == 3:
        edit_name = input('请输入你要修改的名字：')
        x = -1
        for default_card in cards:
            # 每迭代一个字典x+1,第一个字典位置加1后刚好为0
            x += 1
            if edit_name == default_card["name"]:
                name = input("请输入新的姓名：")
                phone = input("请输入新的手机号：")
                address = input("请输入新的地址：")
                business_card = dict()
                business_card["name"] = name
                business_card["phone"] = phone
                business_card["address"] = address
                cards[x] = business_card
    elif num == 4:
        find_name = input("请输入要查找的姓名：")
        find_flag = 0  # 定义一个变量，表示默认的状态为没有找到，用于判断何时结束循环
        for temp in cards:
            if find_name == temp["name"]:
                print("姓名\t手机\t地址")
                print("%s\t%s\t%s" % (temp["name"], temp["phone"], temp["address"]))
                find_flag = 1
                break
        if find_flag == 0:
            print("输入的姓名不存在！")
    elif num == 5:
        print("姓名\t手机\t地址")
        for temp in cards:
            print("%s\t%s\t%s" % (temp["name"], temp["phone"], temp["address"]))
    elif num == 6:
        print("谢谢使用，欢迎再次使用！")
        break
    else:
        print("请输入正确的数字！")

    print(" ")

