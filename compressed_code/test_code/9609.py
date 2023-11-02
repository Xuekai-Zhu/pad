def solution():
    
    fine_amount = 256
    speed_limit = 50
    fine_per_mph_over_limit = 16
    mph_over_limit = (fine_amount / fine_per_mph_over_limit)
    actual_speed = speed_limit + mph_over_limit
    result = actual_speed
    return result

print(solution())