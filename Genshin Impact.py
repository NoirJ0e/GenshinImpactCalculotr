import sys
# 1金币 = 5经验
# 紫书 = 20000 经验 = 4本蓝书 , 蓝书 = 5000 经验

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

character_level_origin = int(input("请输入你的人物想升级到多少级: "))

if character_level_origin == 0:
    exp_needed = 0
elif character_level_origin == 20:
    exp_needed = 9*紫书
elif character_level_origin == 40:
    exp_needed = (6+29)*紫书
elif character_level_origin == 50:
    exp_needed = (6+29+29)*紫书
elif character_level_origin == 50:
    exp_needed = (6+29+29)*紫书
elif character_level_origin == 60:
    exp_needed = (6+29+29+43)*紫书
elif character_level_origin == 70:
    exp_needed = (6+29+29+43+60)*紫书
elif character_level_origin == 80:
    exp_needed = (6+29+29+43+60+81)*紫书
elif character_level_origin == 90:
    exp_needed = (6+29+29+43+60+81+171)*紫书
else:
    print("输入有误!必须为 20,40,50,70或80!请重新运行此程序")
    sys.exit(1)

# 统计现有资源

purple_exp_book_owned = int(input("你现在有多少本紫书: "))
blue_exp_book_owned = int(input("你现在有多少本蓝书: "))
final_exp_needed = int(exp_needed)-int(purple_exp_book_owned)*紫书-int(blue_exp_book_owned)*蓝书

# 计算所需资源

book_needed = final_exp_needed / int(蓝书)
amount_of_exp_flower = final_exp_needed/(2*紫书+6*蓝书)
rein_needed_for_exp = amount_of_exp_flower*20
money_needed_for_exp = final_exp_needed/5
print('\n')

# 用于判断武器升级所需经验的部分

weapon_star_level = int(input("请输入武器星级: "))
weapon_exp_level_origin = int(input("请输入你想将武器升级到多少级: "))

if weapon_star_level == 5:
    if weapon_exp_level_origin == 20:
        weapon_exp_needed = 12150
        resource_fuben = 0
        resource_jingying = 0
    elif weapon_exp_level_origin == 40:
        weapon_exp_needed = 12150+622800
        resource_fuben = 5*绿副本
        resource_jingying = 5*绿精英
    elif weapon_exp_level_origin == 50:
        weapon_exp_needed = 12150+622800+628150
        resource_fuben = 5*蓝副本
        resource_jingying = 18*绿精英
    elif weapon_exp_level_origin == 60:
        weapon_exp_needed = 12150+622800+628150+927675
        resource_fuben = 9*蓝副本
        resource_jingying = 9*蓝精英
    elif weapon_exp_level_origin == 70:
        weapon_exp_needed = 12150+622800+628150+927675+12999125
        resource_fuben = 5*紫副本
        resource_jingying = 18*蓝精英
    elif weapon_exp_level_origin == 80:
        weapon_exp_needed = 12150+622800+628150+927675+12999125+1750375
        resource_fuben = 9*紫副本
        resource_jingying = 14*紫精英
elif weapon_star_level == 4:
    if weapon_exp_level_origin == 20:
        weapon_exp_needed = 81000
    elif weapon_exp_level_origin == 40:
        weapon_exp_needed = 81000+415125
    elif weapon_exp_level_origin == 50:
        weapon_exp_needed = 81000+415125+418725
    elif weapon_exp_level_origin == 60:
        weapon_exp_needed = 81000+415125+418725+618400
    elif weapon_exp_level_origin == 70:
        weapon_exp_needed = 81000+415125+418725+618400+866050
    elif weapon_exp_level_origin == 80:
        weapon_exp_needed = 81000+415125+418725+618400+866050+1166875

#武器升级材料

weapon_exp_stone_blue = weapon_exp_needed/10000
weapon_exp_stone_green = weapon_exp_stone_blue*5
weapon_exp_stone_origin_soure_blue = weapon_exp_stone_blue*4
weapon_exp_stone_origin_soure_green = weapon_exp_stone_green*3


print("\n 你需要 "+str(book_needed)+" 本蓝书,需要刷至少 "+ str(amount_of_exp_flower)+"次地脉之花\n 也就是至少需要"+str(rein_needed_for_exp)+" 点体力和"+str(money_needed_for_exp)+"金币\n")
print(' 你需要'+str(weapon_exp_needed)+' 点经验, 相当于'+str(weapon_exp_stone_blue)+'个蓝矿, '+str(weapon_exp_stone_origin_soure_blue)+' 个水晶矿')
print(' 突破需要 '+str(resource_fuben)+' 个绿副本材料, 相当于至少需要刷 '+str())