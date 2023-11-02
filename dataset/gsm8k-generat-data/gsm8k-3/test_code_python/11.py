def solution():
    """Tobias is buying a new pair of shoes that costs $95. He has been saving up his money each month for the past three months. He gets a $5 allowance a month. He also mows lawns and shovels driveways. He charges $15 to mow a lawn and $7 to shovel. After buying the shoes, he has $15 in change. If he mows 4 lawns, how many driveways did he shovel?"""
    # Define the cost of the shoes
    shoe_cost = 95

    # Define the amount of money saved each month
    monthly_savings = 5

    # Calculate the total amount of money saved
    total_savings = monthly_savings * 3

    # Calculate the total amount of money Tobias has
    tobias_total_money = total_savings + 15

    # Calculate the amount of money Tobias must have had before buying the shoes
    tobias_money_before_shoe_purchase = tobias_total_money + shoe_cost

    # Calculate the amount of money Tobias earned from mowing lawns
    mowing_earnings = 15 * 4

    # Calculate the amount of money Tobias earned from shoveling driveways
    shoveling_earnings = tobias_money_before_shoe_purchase - mowing_earnings - tobias_total_money

    # Calculate the number of driveways Tobias shoveled
    num_driveways_shoveled = shoveling_earnings / 7

    result = num_driveways_shoveled
    return result

print(solution())