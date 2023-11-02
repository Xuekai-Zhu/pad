def solution():
    
    regular_price = 3
    large_price = 5
    regular_count = 221
    large_count = 185
    total_regular_price = regular_price * regular_count
    total_large_price = large_price * large_count
    total_price = total_regular_price + total_large_price
    result = total_price
    return result

print(solution())