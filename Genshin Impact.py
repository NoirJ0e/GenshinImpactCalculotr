import sys
# 1金币 = 5经验
# 紫书 = 20000 经验 = 4本蓝书 , 蓝书 = 5000 经验
# 1金材料 = 3紫材料 = 9蓝材料 = 12绿材料, 3低级材料 = 1高级材料
# 徽记部分
新兵 = 1
士官 = 3*新兵
尉官 = 3*士官

# 材料部分
绿副本 = 1
蓝副本 = 3*绿副本
紫副本 = 3*蓝副本

绿精英 = 1
蓝精英 = 1
紫精英 = 1
#经验部分
蓝书 = 5000
紫书 = 4*蓝书

# 用于判断人物升级经验的部分
character_level= int(input("请输入你的人物现在的等级: "))
character_level_origin = int(input("请输入你的人物想升级到多少级: "))

if character_level == 0:
    exp_origin = 0
elif character_level == 20:
    exp_origin = 9*紫书
elif character_level == 40:
    exp_origin = (6+29)*紫书
elif character_level == 50:
    exp_origin = (6+29+29)*紫书
elif character_level == 50:
    exp_origin = (6+29+29)*紫书
elif character_level == 60:
    exp_origin = (6+29+29+43)*紫书
elif character_level == 70:
    exp_origin = (6+29+29+43+60)*紫书
elif character_level == 80:
    exp_origin = (6+29+29+43+60+81)*紫书
elif character_level == 90:
    exp_origin = (6+29+29+43+60+81+171)*紫书


if character_level_origin == 0:
    exp_needed = 0
elif character_level_origin == 20:
    exp_needed = 9*紫书-int(exp_origin)
elif character_level_origin == 40:
    exp_needed = (6+29)*紫书-int(exp_origin)
elif character_level_origin == 50:
    exp_needed = (6+29+29)*紫书-int(exp_origin)
elif character_level_origin == 50:
    exp_needed = (6+29+29)*紫书-int(exp_origin)
elif character_level_origin == 60:
    exp_needed = (6+29+29+43)*紫书-int(exp_origin)
elif character_level_origin == 70:
    exp_needed = (6+29+29+43+60)*紫书-int(exp_origin)
elif character_level_origin == 80:
    exp_needed = (6+29+29+43+60+81)*紫书-int(exp_origin)
elif character_level_origin == 90:
    exp_needed = (6+29+29+43+60+81+171)*紫书-int(exp_origin)
else:
    print("输入有误!必须为 20,40,50,70或80!请重新运行此程序")
    sys.exit(1)

if int(exp_origin) == int(exp_needed):
    print('已经够了,不用继续刷了')
else:
    purple_exp_book_owned = input("你现在有多少本紫书: ")
    blue_exp_book_owned = input("你现在有多少本蓝书: ")
    final_exp_needed = int(exp_needed)-int(purple_exp_book_owned)*紫书-int(blue_exp_book_owned)*蓝书
    book_needed = final_exp_needed / int(蓝书)
    amount_of_exp_flower = final_exp_needed/(2*紫书+6*蓝书)
    rein_needed_for_exp = amount_of_exp_flower*20


money_needed_for_exp = final_exp_needed/5
print("\n 你需要 "+str(book_needed)+" 本蓝书,需要刷至少 "+ str(amount_of_exp_flower)+"次地脉之花\n 也就是至少需要"+str(rein_needed_for_exp)+" 点体力和"+str(money_needed_for_exp)+"金币\n")
 