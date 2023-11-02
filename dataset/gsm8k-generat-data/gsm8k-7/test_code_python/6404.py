def solution():
    candy_bars = 2
    candy_bar_price = 0.75
    lollipops = 4
    lollipop_price = 0.25

    # Calculate the total cost of candy bars and lollipops
    total_cost = (candy_bars * candy_bar_price) + (lollipops * lollipop_price)

    # Calculate one-sixth of Jimmy's earnings from shoveling snow
    one_sixth_earnings = total_cost

    # Calculate how much Jimmy earns per driveway
    earnings_per_driveway = 1.5

    # Calculate how many driveways Jimmy shoveled
    num_driveways = one_sixth_earnings / earnings_per_driveway
    result = num_driveways
    return result

print(solution())