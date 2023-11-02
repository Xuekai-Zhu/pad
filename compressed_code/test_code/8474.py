def solution():
    
    total_stripes = 13
    red_stripes = (total_stripes - 1) / 2 + 1
    num_flags = 10
    total_red_stripes = red_stripes * num_flags
    result = total_red_stripes
    return result

print(solution())