def solution():
    seconds_in_minute = 60
    minutes_in_hour = 60
    number_of_seconds = 4 * seconds_in_minute
    small_crash_rate = 10
    big_crash_rate = 20
    small_crashes = number_of_seconds / small_crash_rate
    big_crashes = number_of_seconds / big_crash_rate
    total_crashes = small_crashes + big_crashes
    result = total_crashes
    
    return result

print(solution())