def solution():
    # Calculate the number of bricks Tom can buy for 50% off
    half_of_bricks = 1000 / 2
    discount_price = 0.50 * 0.5
    cost_of_discount_bricks = half_of_bricks * discount_price

    # Calculate the cost of the remaining bricks at full price
    remaining_bricks = 1000 - half_of_bricks
    full_price = 0.50
    cost_of_remaining_bricks = remaining_bricks * full_price

    # Calculate the total cost of all the bricks
    total_cost = cost_of_discount_bricks + cost_of_remaining_bricks
    result = total_cost
    return result

print(solution())