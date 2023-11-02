def solution():
    
    starting_temp = 50
    time_elapsed = 8 
    temp_increase_per_hour = 1.5 / 2 
    temp_increase_over_time_elapsed = temp_increase_per_hour * time_elapsed
    final_temp = starting_temp + temp_increase_over_time_elapsed
    result = final_temp
    return result

print(solution())