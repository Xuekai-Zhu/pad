def solution():
    """A bowl of fruit holds 18 peaches. Four of the peaches are ripe and two more ripen every day, but on the third day three are eaten. How many more ripe peaches than unripe peaches are in the bowl after five days?"""
    total_peaches = 18
    ripe_peaches = 4
    days = 5
    unripe_peaches = total_peaches - ripe_peaches
    for i in range(1, days + 1):
        if i == 3:
            ripe_peaches += 2 #two more ripen every day, but on the third day three are eaten.
            ripe_peaches -= 3
        else:
            ripe_peaches += 2
    difference = ripe_peaches - unripe_peaches
    result = difference
    return result

print(solution())