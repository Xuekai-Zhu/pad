def solution():
    
    painting_time = 8
    counter_time = 3 * painting_time
    lawn_time = 6
    hourly_rate = 15
    total_time = painting_time + counter_time + lawn_time
    total_pay = total_time * hourly_rate
    result = total_pay
    return result

print(solution())