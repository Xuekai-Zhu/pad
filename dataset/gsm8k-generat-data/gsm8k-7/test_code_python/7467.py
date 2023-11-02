def solution():
    time_without_AC = 3 # hours
    temp_rise_per_hour = 8 # degrees F
    temp_target = 43 # degrees F
    temp_drop_per_hour = 4 # degrees F
    
    # Find out how much the temperature rose during the power outage
    temp_rise = time_without_AC * temp_rise_per_hour
    
    # Find out how much the temperature needs to drop to reach the target temperature
    temp_drop_needed = temp_rise - (temp_target - 32) # Convert target temp from F to C
    
    # Divide the amount of temperature drop needed by the rate of temperature drop to find the time needed
    time_needed = temp_drop_needed / temp_drop_per_hour
    
    result = time_needed
    return result

print(solution())