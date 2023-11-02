def solution():
    mon_rain = 1.5
    tue_rain = 2.5
    num_mon = 7
    num_tue = 9

    # Calculate total rain on Mondays and Tuesdays
    total_mon_rain = mon_rain * num_mon
    total_tue_rain = tue_rain * num_tue

    # Calculate the difference in rain between Tuesdays and Mondays
    diff = total_tue_rain - total_mon_rain
    result = diff
    return result

print(solution())