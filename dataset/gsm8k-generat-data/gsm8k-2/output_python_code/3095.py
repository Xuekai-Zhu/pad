def solution():
    """Two days ago, the temperature in the morning went up 1.5 degrees every 2 hours. If the temperature was 50 degrees at 3 A.M., what was the temperature at 11 A.M.?"""
    starting_temp = 50
    time_elapsed = 8 # 11AM - 3AM = 8 hours elapsed
    temp_increase_per_hour = 1.5 / 2 # temperature increases 1.5 degrees every 2 hours
    temp_increase_over_time_elapsed = temp_increase_per_hour * time_elapsed
    final_temp = starting_temp + temp_increase_over_time_elapsed
    result = final_temp
    return result

print(solution())