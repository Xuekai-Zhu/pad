def solution():
    total_bricks = 1000
    half_bricks = total_bricks / 2
    half_price = 0.50 * 0.5  # 50% discount

    # Calculate the total cost of half the bricks with 50% discount
    half_cost = half_bricks * half_price

    # Calculate the total cost of the other half of the bricks at full price
    other_half_cost = half_bricks * 0.50

    # Calculate the total cost of all the bricks
    total_cost = half_cost + other_half_cost
    result = total_cost
    return result

print(solution())