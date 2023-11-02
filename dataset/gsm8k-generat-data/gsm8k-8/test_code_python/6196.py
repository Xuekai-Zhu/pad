def solution():
    large_order_peanuts = 200 * 3
    remaining_peanuts = 800 - large_order_peanuts
    small_order_peanuts = remaining_peanuts / 50
    result = small_order_peanuts
    return result

print(solution())