def solution():
    initial_pollywogs = 2400
    rate_of_disappearance = 50
    days_to_disappear = initial_pollywogs // rate_of_disappearance
    
    melvin_catch_rate = 10
    melvin_released = melvin_catch_rate * 20
    
    remaining_pollywogs = initial_pollywogs - (rate_of_disappearance * days_to_disappear)
    days_to_disappear += (remaining_pollywogs // (rate_of_disappearance - melvin_catch_rate)) + 20
    
    result = days_to_disappear
    return result

print(solution())