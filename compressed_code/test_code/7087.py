def solution():
    
    last_week_total = 324
    current_week_total = sum([34, 20, 0, 123, 64, 23])
    difference = last_week_total - current_week_total
    result = difference + 1  
    return result

print(solution())