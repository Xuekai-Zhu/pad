def solution():
    
    laps = 7
    square_length = 3/4
    race_length = laps * square_length
    this_year_time = 42
    last_year_time = 47.25
    this_year_mile_time = this_year_time / race_length
    last_year_mile_time = last_year_time / race_length
    time_difference = last_year_mile_time - this_year_mile_time
    result = time_difference
    return result

print(solution())