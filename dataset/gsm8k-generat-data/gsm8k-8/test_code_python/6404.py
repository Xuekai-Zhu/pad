def solution():
    # Calculate the total cost of the candy bars
    candy_bar_cost = 2 * 0.75

    # Calculate the total cost of the lollipops
    lollipop_cost = 4 * 0.25

    # Calculate the total amount spent
    total_spent = candy_bar_cost + lollipop_cost

    # Calculate the total amount earned from shoveling snow
    total_earned = total_spent * 6

    # Calculate the number of driveways shovelled
    num_driveways = total_earned / 1.5
    result = num_driveways
    return result

print(solution())