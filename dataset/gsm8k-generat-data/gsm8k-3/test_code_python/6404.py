def solution():
    """Jimmy is at the candy store and buys 2 candy bars for $.75 each. He then buys 4 lollipops that cost $.25 each. He spent 1/6 of the money he earned from shoveling snow. If he charges $1.5 per driveway, how many driveways did he shovel?"""
    
    # Calculate the total cost of the candy bars
    candy_cost = 2 * 0.75

    # Calculate the total cost of the lollipops
    lollipop_cost = 4 * 0.25

    # Calculate the total cost of the candy and lollipops
    candy_lollipop_cost = candy_cost + lollipop_cost

    # Calculate the total amount of money Jimmy earned from shoveling snow
    total_money = candy_lollipop_cost * 6

    # Calculate how much money Jimmy spent at the candy store as a fraction of his snow shoveling earnings
    candy_spending_fraction = candy_lollipop_cost / total_money

    # Calculate how much money Jimmy earned for each driveway he shoveled
    driveway_earnings = 1.5

    # Calculate how many driveways Jimmy shoveled
    num_driveways = int(candy_spending_fraction / driveway_earnings)

    # Display the number of driveways Jimmy shoveled
    result = num_driveways
    return result

print(solution())