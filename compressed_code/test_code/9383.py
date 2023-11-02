def solution():
    
    regular_bottle_size = 16
    extra_bottle_size = regular_bottle_size * 1.25
    regular_bottles_per_day = 16 // 4  
    extra_bottles_per_day = 2
    total_fluid_per_day = (regular_bottle_size * regular_bottles_per_day) + (extra_bottle_size * extra_bottles_per_day)
    total_fluid_per_week = total_fluid_per_day * 7
    result = total_fluid_per_week
    return result

print(solution())