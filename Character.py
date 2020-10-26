import sys
# 1金币 = 5经验
# purple_exp_book = 20000 经验 = 4本blue_exp_book , blue_exp_book = 5000 经验
# 1金材料 = 3紫材料 = 9蓝材料 = 12绿材料, 3低级材料 = 1高级材料

# 材料部分
green_instance = 1
blue_instance = 3*green_instance
purple_instance = 3*blue_instance

green_elite = 1
blue_elite = 3*green_elite
purple_elite = 3*blue_elite
#经验部分
blue_exp_book = 5000
purple_exp_book = 4*blue_exp_book
print(purple_exp_book)
# 用于判断人物升级经验的部分
character_level= int(input("请输入你的人物现在的等级: "))
character_level_origin = int(input("请输入你的人物想升级到多少级: "))

if character_level == 0:
    exp_origin = 0
elif character_level == 20:
    exp_origin = 9*purple_exp_book
elif character_level == 40:
    exp_origin = (6+29)*purple_exp_book
elif character_level == 50:
    exp_origin = (6+29+29)*purple_exp_book
elif character_level == 50:
    exp_origin = (6+29+29)*purple_exp_book
elif character_level == 60:
    exp_origin = (6+29+29+43)*purple_exp_book
elif character_level == 70:
    exp_origin = (6+29+29+43+60)*purple_exp_book
elif character_level == 80:
    exp_origin = (6+29+29+43+60+81)*purple_exp_book
elif character_level == 90:
    exp_origin = (6+29+29+43+60+81+171)*purple_exp_book


if character_level_origin == 0:
    exp_needed = 0
elif character_level_origin == 20:
    exp_needed = 9*purple_exp_book-int(exp_origin)
elif character_level_origin == 40:
    exp_needed = (6+29)*purple_exp_book-int(exp_origin)
elif character_level_origin == 50:
    exp_needed = (6+29+29)*purple_exp_book-int(exp_origin)
elif character_level_origin == 50:
    exp_needed = (6+29+29)*purple_exp_book-int(exp_origin)
elif character_level_origin == 60:
    exp_needed = (6+29+29+43)*purple_exp_book-int(exp_origin)
elif character_level_origin == 70:
    exp_needed = (6+29+29+43+60)*purple_exp_book-int(exp_origin)
elif character_level_origin == 80:
    exp_needed = (6+29+29+43+60+81)*purple_exp_book-int(exp_origin)
elif character_level_origin == 90:
    exp_needed = (6+29+29+43+60+81+171)*purple_exp_book-int(exp_origin)
else:
    print("输入有误!必须为 20,40,50,70或80!请重新运行此程序")
    sys.exit(1)

if int(exp_origin) > int(exp_needed):
    print('已经够了,不用继续刷了')
else:
    purple_exp_book_owned = input("你现在有多少本紫书: ")
    blue_exp_book_owned = input("你现在有多少本蓝书: ")
    final_exp_needed = int(exp_needed)-int(purple_exp_book_owned)*purple_exp_book-int(blue_exp_book_owned)*blue_exp_book
    book_needed = final_exp_needed / int(blue_exp_book)
    amount_of_exp_flower = final_exp_needed/(2*purple_exp_book+6*blue_exp_book)
    rein_needed_for_exp = amount_of_exp_flower*20
    money_needed_for_exp = final_exp_needed/5
    print("\n 你需要 "+str(book_needed)+" 本蓝书,需要刷至少 "+ str(amount_of_exp_flower)+"次地脉之花\n 也就是至少需要"+str(rein_needed_for_exp)+" 点体力和"+str(money_needed_for_exp)+"金币\n")

 