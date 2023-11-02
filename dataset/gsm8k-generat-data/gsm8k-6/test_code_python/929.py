def solution():
    # Calculate the total cost of the bricks Tom needs to buy
    half_bricks = 1000 / 2
    cost_half_bricks = (0.5 * 0.5 * half_bricks) * 0.5  # 50% off of $.50
    cost_other_half_bricks = 0.5 * half_bricks  # full price
    total_cost = cost_half_bricks + cost_other_half_bricks
    result = total_cost
    return result

print(solution())