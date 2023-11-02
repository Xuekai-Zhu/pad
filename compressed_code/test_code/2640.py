def solution():
    
    total_flags = 10
    total_stripes = total_flags * 13
    red_stripes = 1
    for i in range(1, 13):
        red_stripes += (total_stripes - i) % 2
    result = red_stripes * total_flags
    return result

print(solution())