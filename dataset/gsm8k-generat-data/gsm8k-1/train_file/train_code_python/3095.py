def solution():
    """Two days ago, the temperature in the morning went up 1.5 degrees every 2 hours. If the temperature was 50 degrees at 3 A.M., what was the temperature at 11 A.M.?"""
    starting_temp = 50
    time_difference = 8
    rate_of_change = 1.5 / 2
    temp_change = rate_of_change * time_difference
    final_temp = starting_temp + temp_change
    result = final_temp
    return result

print(solution())