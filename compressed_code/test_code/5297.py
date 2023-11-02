def solution():
    
    small_price = 3
    large_price = 5
    small_count = 8
    budget = 50
    change = 1
    
    total_small_price = small_price * small_count
    remaining_budget = budget - total_small_price - change
    large_count = remaining_budget // large_price
    
    result = large_count
    return result

print(solution())