# 定义材料

# 副本材料
green_instance = 1
blue_instance = 3*green_instance
purple_instance = 3*blue_instance
gold_instance = 3*purple_instance
# 怪物材料
green_elite = 1
blue_elite = 3*green_elite
purple_elite = 3*blue_instance
gold_elite = 3*purple_elite
# 人物经验书
green_exp_book = 1000
blue_exp_book = 5*green_exp_book
purple_exp_book = 4*blue_exp_book
# 武器经验
green_exp_stone = 2000
blue_exp_stone = 10000

# 获取玩家世界等级
world_level = int(input('请输入你的世界等级: '))
while 0 <= world_level <= 5:
    break
else:
    print('输入有误! 请重新输入!')
    world_level = int(input('请输入你的世界等级: '))
# 定义一朵经验花能最少能给予多少经验
# 资料来源: http://www.pt212.com/d/file/96kaifa/202010170817/1600075739_3.jpg
if world_level == 0:
    exp_flower = 7*green_exp_book+2*blue_exp_book
elif world_level == 1:
    exp_flower == 8*green_exp_book+5*blue_exp_book
elif world_level == 2:
    exp_flower = 10*blue_exp_book
elif world_level == 3:
    exp_flower = 13*blue_exp_book
elif world_level == 4:
    exp_flower = 6*blue_exp_book+2*purple_exp_book
elif world_level == 5:
    exp_flower = 7*blue_exp_book+3*purple_exp_book

# 定义角色等级
character_level_origin = int(input('请输入你的角色等级(暂时只有0,20,40,50,60,80,90可用): '))
while 0 <= character_level_origin <= 80:
    break
else:
    print('不合理的输入! 请重新输入!')

character_level_want = int(input('请输入你想将角色升到多少级(暂时只有20,40,50,60,80,90可用): '))
while 20 <= character_level_want <= 90:
    break
else:
    print('不合理的输入! 请重新输入!')
    character_level_want = int(input('请输入你想将角色升到多少级(暂时只有20,40,50,60,80,90可用): '))

# 定义已经拥有的经验
if character_level_origin == 0:
    exp_owned = 0
elif character_level_origin == 20:
    exp_owned = 9*purple_exp_book
elif character_level_origin == 40:
    exp_owned = (6+29)*purple_exp_book
elif character_level_origin == 50:
    exp_owned = (6+29+29)*purple_exp_book
elif character_level_origin == 60:
    exp_owned = (6+29+29+43)*purple_exp_book
elif character_level_origin == 70:
    exp_owned = (6+29+29+43+60)*purple_exp_book
elif character_level_origin == 80:
    exp_owned = (6+29+29+43+60+81)*purple_exp_book
elif character_level_origin == 90:
    exp_owned = (6+29+29+43+60+81+171)*purple_exp_book

# 定义需要的经验
if character_level_want == 20:
    exp_needed = 9*purple_exp_book - int(exp_owned)
elif character_level_want == 40:
    exp_needed = (6+29)*purple_exp_book - int(exp_owned)
elif character_level_want == 50:
    exp_needed = (6+29+29)*purple_exp_book - int(exp_owned)
elif character_level_want == 60:
    exp_needed = (6+29+29+43)*purple_exp_book - int(exp_owned)
elif character_level_want == 70:
    exp_needed = (6+29+29+43+60)*purple_exp_book - int(exp_owned)
elif character_level_want == 80:
    exp_needed = (6+29+29+43+60+81)*purple_exp_book - int(exp_owned)
elif character_level_want == 100:
    exp_needed = (6+29+29+43+60+81+171)*purple_exp_book - int(exp_owned)

if exp_needed <= 0:
    print('输入有误')
else:
    exp_needed = exp_needed

# 收集现有的经验量
purple_exp_book_owned = int(input('请输入你现在拥有的紫书: '))
blue_exp_book_owned = int(input('请输入你现在有多少本蓝书'))
exp_owned_by_book = purple_exp_book*purple_exp_book_owned+blue_exp_book*blue_exp_book_owned
# 刷的经验花数量
amount_of_exp_flower = (exp_needed - exp_owned_by_book) / exp_flower
print(amount_of_exp_flower)
