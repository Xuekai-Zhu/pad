def solution():
    candy_bars = 2  # Jimmy bought 2 candy bars
    candy_bar_price = 0.75  # Candy bars cost $0.75 each
    lollipops = 4  # Jimmy bought 4 lollipops
    lollipop_price = 0.25  # Lollipops cost $0.25 each

    # Calculate the total money Jimmy spent on candy and lollipops
    total_spent = (candy_bars * candy_bar_price) + (lollipops * lollipop_price)

    # Calculate the total money Jimmy earned from shoveling snow
    total_earned = total_spent * 6  # Jimmy spent 1/6 of his snow shoveling earnings

    # Calculate how many driveways Jimmy shoveled
    driveways_shoveled = total_earned / 1.5  # Jimmy charges $1.5 per driveway

    result = driveways_shoveled
    return result

print(solution())