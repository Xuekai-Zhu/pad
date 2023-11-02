def solution():
    
    mowing_lines = 40
    mowing_time_per_line = 2
    total_mowing_time = mowing_lines * mowing_time_per_line
    flower_rows = 8
    flowers_per_row = 7
    flower_time_per_flower = 0.5
    total_flower_time = flower_rows * flowers_per_row * flower_time_per_flower
    total_gardening_time = total_mowing_time + total_flower_time
    result = total_gardening_time
    return result

print(solution())