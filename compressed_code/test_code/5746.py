def solution():
    
    total_apples = 405
    used_apples = 90 + 60
    remaining_apples = total_apples - used_apples
    bags_sold = remaining_apples / 5
    price_per_bag = 408 / bags_sold
    result = price_per_bag
    return result

print(solution())