def solution():
    """Tobias is buying a new pair of shoes that costs $95. He has been saving up his money each month for the past three months. He gets a $5 allowance a month. He also mows lawns and shovels driveways. He charges $15 to mow a lawn and $7 to shovel. After buying the shoes, he has $15 in change. If he mows 4 lawns, how many driveways did he shovel?"""
    # Define the cost of the shoes and Tobias' savings
    shoe_cost = 95
    savings = 3 * 5

    # Calculate Tobias' total income from mowing lawns and shoveling driveways
    lawn_income = 4 * 15
    total_income = lawn_income + savings + 15  # his change after buying the shoes

    # Calculate the amount left after buying the shoes
    left_over = total_income - shoe_cost

    # Calculate the number of driveways he shoveled
    num_driveways = (left_over - (4 * 15)) / 7

    result = int(num_driveways)
    return result

print(solution())