def solution():
    # Calculate the cost of buying half the bricks for 50% off
    half_bricks = 1000 / 2
    cost_half_bricks = half_bricks * 0.50 * 0.5  # 50% off of $0.50

    # Calculate the cost of buying the other half of the bricks at full price
    other_half_bricks = half_bricks
    cost_other_half_bricks = other_half_bricks * 0.50  # $0.50 per brick

    # Calculate the total cost of all the bricks
    total_cost = cost_half_bricks + cost_other_half_bricks
    result = total_cost
    return result

print(solution())