def solution():
    
    hourly_pay = 5
    vacuuming_time = 2 * 2
    dishes_time = 0.5
    bathroom_time = 3 * dishes_time
    total_time = vacuuming_time + dishes_time + bathroom_time
    total_pay = total_time * hourly_pay
    result = total_pay
    return result

print(solution())