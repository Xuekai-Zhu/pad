def solution():
    """Tobias is buying a new pair of shoes that costs $95. He has been saving up his money each month for the past three months. He gets a $5 allowance a month. He also mows lawns and shovels driveways. He charges $15 to mow a lawn and $7 to shovel. After buying the shoes, he has $15 in change. If he mows 4 lawns, how many driveways did he shovel?"""
    shoe_cost = 95
    allowance = 5 * 3
    lawn_money = 15 * 4
    total_savings = allowance + lawn_money
    remaining_money = total_savings - shoe_cost + 15
    num_driveways_shoveled = (remaining_money // 7)  # using floor division to get whole number of driveways
    result = num_driveways_shoveled
    return result

print(solution())