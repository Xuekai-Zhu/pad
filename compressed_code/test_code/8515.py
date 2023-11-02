def solution():
    
    mowing_lines = 40
    time_per_mow = 2
    flower_rows = 8
    flowers_per_row = 7
    time_per_flower = 0.5
    total_time = (mowing_lines * time_per_mow) + (flower_rows * flowers_per_row * time_per_flower)
    result = total_time
    return result

print(solution())