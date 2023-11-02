def solution():
    
    painting_time = 8
    counter_fixing_time = 3 * painting_time
    lawn_mowing_time = 6
    total_time = painting_time + counter_fixing_time + lawn_mowing_time
    hourly_rate = 15
    total_payment = total_time * hourly_rate
    result = total_payment
    return result

print(solution())