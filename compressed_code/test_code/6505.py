def solution():
    
    total_bricks = 1000
    half_bricks = total_bricks / 2
    half_price = 0.50 * 0.5
    half_cost = half_bricks * half_price
    full_bricks = total_bricks / 2
    full_price = 0.50
    full_cost = full_bricks * full_price
    total_cost = half_cost + full_cost
    result = total_cost
    return result

print(solution())