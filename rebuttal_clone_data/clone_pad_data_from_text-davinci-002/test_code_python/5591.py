def solution():
    current_time = 10
    end_time = 90
    days = 1
    while current_time < end_time:
        current_time += 10
        days += 1
    result = days
    
    return result

print(solution())