def solution():
    
    small_bulbs_needed = 3
    large_bulbs_needed = 1
    small_bulb_cost = 8
    large_bulb_cost = 12
    total_cost = (small_bulbs_needed * small_bulb_cost) + (large_bulbs_needed * large_bulb_cost)
    money_left = 60 - total_cost
    result = money_left
    return result

print(solution())