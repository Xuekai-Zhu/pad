def solution():
    
    hot_tub_size = 40 * 4 
    bottle_size = 1 
    bottle_cost = 50
    discount_percent = 20
    total_bottles = hot_tub_size / bottle_size
    discounted_total_cost = total_bottles * bottle_cost * (1 - discount_percent/100)
    result = discounted_total_cost
    return result

print(solution())