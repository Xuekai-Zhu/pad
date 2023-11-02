def solution():
    # Calculate the total time it was raining on the first day
    first_day_rain_time = 10  # it rained from 7:00 AM to 5:00 PM, which is 10 hours

    # Calculate the total time it was raining on the second day
    second_day_rain_time = first_day_rain_time + 2  # it took 2 more hours than the first day to stop

    # Calculate the total time it was raining on the third day
    third_day_rain_time = second_day_rain_time * 2  # it poured for twice the time it took on the second day

    # Calculate the total time it was raining in the three days
    total_rain_time = first_day_rain_time + second_day_rain_time + third_day_rain_time
    result = total_rain_time
    return result

print(solution())