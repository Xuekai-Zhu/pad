def solution():
    """Jimmy is at the candy store and buys 2 candy bars for $.75 each. He then buys 4 lollipops that cost $.25 each. He spent 1/6 of the money he earned from shoveling snow. If he charges $1.5 per driveway, how many driveways did he shovel?"""
    candy_bar_cost = 0.75
    lollipop_cost = 0.25
    candy_bar_quantity = 2
    lollipop_quantity = 4
    candy_bar_total_cost = candy_bar_cost * candy_bar_quantity
    lollipop_total_cost = lollipop_cost * lollipop_quantity
    total_spent = candy_bar_total_cost + lollipop_total_cost
    snow_money_fraction = 1 / 6
    snow_money_earned = total_spent / snow_money_fraction
    driveway_cost = 1.5
    driveways_shoveled = snow_money_earned / driveway_cost
    result = driveways_shoveled
    return result

print(solution())