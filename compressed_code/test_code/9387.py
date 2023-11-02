def solution():
    
    augustus_rate = 3
    luna_rate = 7
    total_time = 8
    augustus_total = augustus_rate * total_time
    luna_total = luna_rate * total_time
    total_milkshakes = augustus_total + luna_total
    result = total_milkshakes
    return result

print(solution())