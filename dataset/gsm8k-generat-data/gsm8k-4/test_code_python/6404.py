def solution():
    """Jimmy is at the candy store and buys 2 candy bars for $.75 each. He then buys 4 lollipops that cost $.25 each. He spent 1/6 of the money he earned from shoveling snow. If he charges $1.5 per driveway, how many driveways did he shovel?"""
    # Define the cost of candy bars and lollipops
    candy_cost = 0.75
    lollipop_cost = 0.25

    # Calculate the total amount spent at the candy store
    total_spent = 2 * candy_cost + 4 * lollipop_cost

    # Calculate the total amount earned from shoveling snow
    total_earned = total_spent * 6

    # Calculate the portion of money spent at the candy store
    candy_portion = total_spent / total_earned

    # Calculate the number of driveways shoveled
    driveways = round(1.5 / (1 - candy_portion))

    # return the result
    result = driveways
    return result

print(solution())