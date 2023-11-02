def solution():
    
    starting_temp = 50
    time_difference = 8
    rate_of_change = 1.5 / 2
    temp_change = rate_of_change * time_difference
    final_temp = starting_temp + temp_change
    result = final_temp
    return result

print(solution())