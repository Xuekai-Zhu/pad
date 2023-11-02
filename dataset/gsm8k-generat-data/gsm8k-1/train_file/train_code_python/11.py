def solution():
    """Tobias is buying a new pair of shoes that costs $95. He has been saving up his money each month for the past three months. 
    He gets a $5 allowance a month. He also mows lawns and shovels driveways. He charges $15 to mow a lawn and $7 to shovel. 
    After buying the shoes, he has $15 in change. If he mows 4 lawns, how many driveways did he shovel?"""
    shoe_cost = 95
    allowance = 5 * 3
    lawn_money = 15 * 4
    remaining_money = 15 + allowance + lawn_money
    total_money = remaining_money + shoe_cost
    driveway_money = total_money % 7
    driveways = driveway_money // 7
    result = driveways
    return result

print(solution())