def solution():
    total_bricks_needed = 1000
    discount_bricks = total_bricks_needed / 2
    full_price_bricks = total_bricks_needed - discount_bricks
    discount_price = 0.5 * 0.5
    full_price = 0.5
    total_price = (discount_bricks * discount_price) + (full_price_bricks * full_price)
    result = total_price
    return result

print(solution())