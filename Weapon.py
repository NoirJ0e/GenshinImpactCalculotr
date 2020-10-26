# 材料部分
green_instance = 1
blue_instance = 3*green_instance
purple_instance = 3*blue_instance

green_elite = 1
blue_elite = 3*green_elite
purple_elite = 3*blue_elite


weapon_star_level = int(input("请输入武器星级: "))
weapon_exp_level_had = int(input("请输入你现在的武器等级: "))
weapon_exp_level_want = int(input("请输入你想将武器升级到多少级: "))

# 用于计算已经投入了多少
if weapon_star_level == 5:
    if weapon_exp_level_had == 20:
        weapon_exp_needed = 12150
        resource_instance = 0
        resource_jingying = 0
    elif weapon_exp_level_had == 40:
        weapon_exp_needed = 12150+622800
        resource_instance = 5*green_instance
        resource_jingying = 5*green_elite
    elif weapon_exp_level_had == 50:
        weapon_exp_needed = 12150+622800+628150
        resource_instance = 5*blue_instance
        resource_jingying = 18*green_elite
    elif weapon_exp_level_had == 60:
        weapon_exp_needed = 12150+622800+628150+927675
        resource_instance = 9*blue_instance
        resource_jingying = 9*blue_elite
    elif weapon_exp_level_had == 70:
        weapon_exp_needed = 12150+622800+628150+927675+12999125
        resource_instance = 5*purple_instance
        resource_jingying = 18*blue_elite
    elif weapon_exp_level_had == 80:
        weapon_exp_needed = 12150+622800+628150+927675+12999125+1750375
        resource_instance = 9*purple_instance
        resource_jingying = 14*purple_elite
elif weapon_star_level == 4:
    if weapon_exp_level_had == 20:
        weapon_exp_needed = 81000
    elif weapon_exp_level_had == 40:
        weapon_exp_needed = 81000+415125
    elif weapon_exp_level_had == 50:
        weapon_exp_needed = 81000+415125+418725
    elif weapon_exp_level_had == 60:
        weapon_exp_needed = 81000+415125+418725+618400
    elif weapon_exp_level_had == 70:
        weapon_exp_needed = 81000+415125+418725+618400+866050
    elif weapon_exp_level_had == 80:
        weapon_exp_needed = 81000+415125+418725+618400+866050+1166875

# 用于计算将要投入多少
if weapon_star_level == 5:
    if weapon_exp_level_want == 20:
        weapon_exp_needed = 12150
        resource_instance = 0
        resource_jingying = 0
    elif weapon_exp_level_want == 40:
        weapon_exp_needed = 12150+622800
        resource_instance = 5*green_instance
        resource_jingying = 5*green_elite
    elif weapon_exp_level_want == 50:
        weapon_exp_needed = 12150+622800+628150
        resource_instance = 5*blue_instance
        resource_jingying = 18*green_elite
    elif weapon_exp_level_want == 60:
        weapon_exp_needed = 12150+622800+628150+927675
        resource_instance = 9*blue_instance
        resource_jingying = 9*blue_elite
    elif weapon_exp_level_want == 70:
        weapon_exp_needed = 12150+622800+628150+927675+12999125
        resource_instance = 5*purple_instance
        resource_jingying = 18*blue_elite
    elif weapon_exp_level_want == 80:
        weapon_exp_needed = 12150+622800+628150+927675+12999125+1750375
        resource_instance = 9*purple_instance
        resource_jingying = 14*purple_elite
elif weapon_star_level == 4:
    if weapon_exp_level_want == 20:
        weapon_exp_needed = 81000
    elif weapon_exp_level_want == 40:
        weapon_exp_needed = 81000+415125
    elif weapon_exp_level_want == 50:
        weapon_exp_needed = 81000+415125+418725
    elif weapon_exp_level_want == 60:
        weapon_exp_needed = 81000+415125+418725+618400
    elif weapon_exp_level_want == 70:
        weapon_exp_needed = 81000+415125+418725+618400+866050
    elif weapon_exp_level_want == 80:
        weapon_exp_needed = 81000+415125+418725+618400+866050+1166875

#武器升级材料

weapon_exp_stone_blue = int(weapon_exp_needed)/10000
weapon_exp_stone_green = weapon_exp_stone_blue*5
weapon_exp_stone_origin_soure_blue = weapon_exp_stone_blue*4
weapon_exp_stone_origin_soure_green = weapon_exp_stone_green*3


print(' 你需要'+str(weapon_exp_needed)+' 点经验, 相当于'+str(weapon_exp_stone_blue)+'个蓝矿, '+str(weapon_exp_stone_origin_soure_blue)+' 个水晶矿')
print(' 突破需要 '+str(resource_instance)+' 个green_instance材料, 相当于至少需要刷 '+str())