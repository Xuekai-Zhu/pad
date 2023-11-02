def solution():
    """Jimmy is at the candy store and buys 2 candy bars for $.75 each. He then buys 4 lollipops that cost $.25 each. He spent 1/6 of the money he earned from shoveling snow. If he charges $1.5 per driveway, how many driveways did he shovel?"""
    candy_bars_cost = 0.75 * 2
    lollipops_cost = 0.25 * 4
    total_spent = candy_bars_cost + lollipops_cost
    snow_money = total_spent * 6
    driveways = int(snow_money / 1.5)
    result = driveways
    return result

print(solution())