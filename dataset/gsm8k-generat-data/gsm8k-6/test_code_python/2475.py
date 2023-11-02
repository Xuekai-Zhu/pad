def solution():
    # Calculate the cost of each lollipop
    cost_per_lollipop = 3 / 12  # Sarah bought 12 lollipops for a total of 3 dollars

    # Calculate the cost of the lollipops shared with Julie
    cost_shared = cost_per_lollipop * (12 / 4)  # Sarah shared one-quarter of the lollipops with Julie

    # Convert the cost to cents
    cents_shared = cost_shared * 100

    result = cents_shared
    return result

print(solution())