#import sys
GEB = 1000
BEB = 5*GEB
PEB = 4*BEB
charLevelOrigin = int(input('Please enter the character currently (Only support 1,20,40,50,60,70.80) : '))
x = charLevelOrigin
print('\nEXP owned has been calculated\n')
if x == 1:
    exp_owned = 0
elif x == 20:
    exp_owned = 120175
elif x == 40:
    exp_owned = 698500
elif x == 50:
    exp_owned = 1277600
elif x == 60:
    exp_owned = 2131725
elif x == 70:
    exp_owned = 3327650
elif x == 80:
    exp_owned = 4939525
elif x == 90:
    exp_owned = 8362650
else:
    print("Wrong input")

charLevelWant = int(input('Please enter the character level you want to reach (Only support 1,20,40,50,60,70.80) : '))
y = charLevelWant
print('\nEXP need has been calculated\n')
if y == 1:
    exp_need = 0
elif y == 20:
    exp_need = 120175
elif y == 40:
    exp_need = 698500
elif y == 50:
    exp_need = 1277600
elif y == 60:
    exp_need = 2131725
elif y == 70:
    exp_need = 3327650
elif y == 80:
    exp_need = 4939525
elif y == 90:
    exp_need = 8362650
else:
    print("Wrong input")

actEXP = exp_need - exp_owned
print('ACTUALLY EXP NEEDED HAS BEEN CALCULATED\n\n')

z = int(input('Please enter your current AR: '))
if z <= 14:
    worldLevel = 0
elif 15 <= z <= 20:
    worldLevel = 1
elif 20 <= z <= 25:
    worldLevel = 2
elif 25 <= z <= 30:
    worldLevel = 3
elif 30 <= z <= 35:
    worldLevel = 4
elif 35 <= z <= 40:
    worldLevel = 5
elif 40 <= z <= 45:
    worldLevel = 6
elif 45 <= z <= 50:
    worldLevel = 7
elif 50 <= z <= 55:
    worldLevel = 8
elif 50 <= z <= 60:
    worldLevel = 8
else:
    print("Wrong input")
print("\nCurrent World Level is:",worldLevel)

if worldLevel == 0:
    monaFlower = 12000
    expFlower = 22000
elif worldLevel == 1:
    monaFlower = 20000
    expFlower - 35000
elif worldLevel == 2:
    monaFlower = 28000
    expFlower = 50000
elif worldLevel == 3:
    monaFlower = 36000
    expFlower = 65000
elif worldLevel == 4:
    monaFlower = 44000
    expFlower = 70000
elif worldLevel == 5:
    monaFlower = 52000
    expFlower = 90000
elif worldLevel == 6:
    monaFlower = 60000
    expFlower = 110000
# 2020.12.13 ,currently it's the same
elif worldLevel == 7:
    monaFlower = 60000
    expFlower = 110000
elif worldLevel == 8:
    monaFlower = 60000
    expFlower = 110000

exp_flower_need = actEXP / expFlower
