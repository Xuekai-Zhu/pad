def solution():
    minutes_in_an_hour = 60
    minutes_in_a_sunset = 2 * minutes_in_an_hour
    minutes_between_colors = 10
    number_of_colors = minutes_in_a_sunset / minutes_between_colors
    result = number_of_colors
    return result

print(solution())