def solution():
    
    days = 5
    initial_time = 5
    total_time = 0
    for i in range(days):
        total_time += initial_time
        initial_time *= 2
    result = total_time
    return result

print(solution())