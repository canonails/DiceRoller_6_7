import random

number_rolls = 100

print("=== Rolling 7 dice once ===")
number_dice = 7
dice_rolls = []
for n in range(number_rolls):
    roll = []
    for i in range(number_dice):
        roll.append(random.randrange(1,7))
    dice_rolls.append(roll)

res_of_7 = []
for r in dice_rolls:
    r_sum = 0
    for d in r:
        r_sum += d
    total = "\t".join(map(str, r)) + "\t" + str(r_sum)
    res_of_7.append(total)

with(open("dice_7.csv", "w") as out):
    for dr in res_of_7:
        out.write(dr + "\n")


# Rolling 6 dice once, re-rolling lowest once
print("=== Rolling 6 dice once, re-rolling lowest once ===")
number_dice = 6
dice_rolls = []
for n in range(number_rolls):
    roll = []
    for i in range(number_dice):
        roll.append(random.randrange(1,7))
    roll.sort()
    roll.pop(0)
    roll.append(random.randrange(1,7))
    dice_rolls.append(roll)

res_of_6 = []
for r in dice_rolls:
    r_sum = 0
    for d in r:
        r_sum += d
    total = "\t".join(map(str, r)) + "\t" + str(r_sum)
    res_of_6.append(total)

with(open("dice_6.csv", "w") as out):
    for dr in res_of_6:
        out.write(dr + "\n")
