def solution():
    # Calculate the total amount Jimmy spent at the candy store
    candy_cost = 2 * 0.75  # 2 candy bars for $.75 each
    lollipop_cost = 4 * 0.25  # 4 lollipops that cost $.25 each
    total_cost = candy_cost + lollipop_cost

    # Calculate the total amount Jimmy earned from shoveling snow
    fraction_spent = 1/6
    total_earned = total_cost / fraction_spent

    # Calculate the number of driveways Jimmy shoveled
    price_per_driveway = 1.5
    num_driveways = total_earned / price_per_driveway
    result = num_driveways
    return result

print(solution())