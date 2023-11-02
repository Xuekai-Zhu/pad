def solution():
    minutes_in_an_hour = 60
    minutes_left_missouri = 7 * minutes_in_an_hour
    minutes_first_stop = 25
    minutes_second_stop = 10
    minutes_third_stop = 25
    minutes_travel_time = minutes_left_missouri + minutes_first_stop + minutes_second_stop + minutes_third_stop
    hours_travel_time = minutes_travel_time / minutes_in_an_hour
    result = hours_travel_time
    return result

print(solution())