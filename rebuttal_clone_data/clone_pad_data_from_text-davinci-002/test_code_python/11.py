def solution():
    """Tobias is buying a new pair of shoes that costs $95. He has been saving up his money each month for the past three months. He gets a $5 allowance a month. He also mows lawns and shovels driveways. He charges $15 to mow a lawn and $7 to shovel. After buying the shoes, he has $15 in change. If he mows 4 lawns, how many driveways did he shovel?"""
    cost_of_shoes = 95
    monthly_allowance = 5
    cost_of_lawnmowing = 15
    cost_of_shoveling = 7
    money_saved = monthly_allowance * 3
    money_leftover = money_saved - cost_of_shoes
    lawns_mowed = 4
    driveways_shoveled = money_leftover / cost_of_shoveling
    result = driveways_shoveled
    return result

print(solution())