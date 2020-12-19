'''
参与计算的套装有:
    1. 水2+宗室2
    2. 水2+乐团2
    3. 水2+角斗2
    4. 角斗2+乐团2
    5. 角斗2+宗室2
    6. 宗室2+乐团2

参与计算的武器有: 弓藏(0精),苍翠猎弓(0精),绝弦(0精),天空弓(0精),Amos(0精),且均为80级
明确一下伤害公式
{基础攻击力+[基础攻击力*(攻击力加成)]+羽毛}*技能伤害倍率*[1-(怪物等级+100)/(怪物等级+人物等级+200)]*怪物抗性*反应系数*对应伤害加成
本次计算的对象为 89级 的 遗迹守卫, 遗迹守卫的七元素抗性为10%,物理抗性为70%

公子仅需要8.5s至9s的时间即可完成三套平A输出循环(可以使三套纯平A或AAA重击循环)

以下所有的数据均为6级技能时候的数据

模拟的输出循环为: 挂火-远程弓大-切近战形态进行三轮攻击循环(忽视技能开启时的伤害)

为了方便计算,这里所有的攻击力加成统一为90%, 都携带一个水伤杯
使用的角色为80级未突破公子
'''
class char:
    def __init__(self, atk, criticrate, criticdmg, elementdmg,mastery):
        self.atk = atk
        self.criticrate = criticrate
        self.criticdmg = criticdmg
        self.elementdmg = elementdmg
        self.mastery = mastery
Char1 = char(266+590,50,150,0.684,0) #天空
Char2 = char(266+532,50,130,0.684,0) #Amos
Char3 = char(266+449,55,130,0.684,0) #苍翠
Char4 = char(266+449,50,130,0.684,0) #弓藏
Char5 = char(266+449,50,130,0.684,151) #绝弦

BowBrust = 5.3
NormalATK = int((56.5+60.5+81.9+87.1+80.4+51.5+54.8)/100)
ChargeATK = int((56.5+60.5+81.9+87.1+80.4+87.5+104.6)/100)

w4 = input('是否使用了风4减抗? 如果是,输入True :')
if w4 == True:
    r = float(-0.3)
else:
    r = float(0.1)

M_d = int(1-(89+100)/(89+80+200))*(1-r)
w2 = input('是否使用了水2? 如果是,输入True : ')

if w2 == True:
    W = float(0.15)
else:
    W = float(0)


#Board1 = (Char1.atk*1.9+311)*(1.682+W)
#Board2 = (Char2.atk*1.9+311)*(1.682+W)
#Board3 = (Char3.atk*1.9+311)*(1.682+W)
#Board4 = (Char4.atk*1.9+311)*(1.682+W)
#Board5 = (Char5.atk*1.9+311)*(1.682+W)
print(char.Char1)
