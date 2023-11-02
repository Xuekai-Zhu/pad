def solution():
    inches_of_rain_per_day = 2
    days_left_in_the_year = 100
    inches_of_rain_so_far = 430
    inches_of_rain_needed = (inches_of_rain_per_day * days_left_in_the_year) - inches_of_rain_so_far
    result = inches_of_rain_needed
    return result

print(solution())