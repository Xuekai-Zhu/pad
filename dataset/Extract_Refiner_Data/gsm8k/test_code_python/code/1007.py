def solution():
    
    tank_capacity = 18000
    wanda_filled = tank_capacity * (1/4)
    ms_b_pumped = wanda_filled * (3/4)
    wanda_remaining = wanda_filled - ms_b_pumped
    ms_b_remaining = tank_capacity * (2/3)
    total_water_pumped = wanda_remaining + ms_b_remaining
    result = total_water_pumped
    return result

print(solution())