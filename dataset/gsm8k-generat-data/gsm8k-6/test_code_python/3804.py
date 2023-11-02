def solution():
    # Calculate the difference between the recommended sleep and actual sleep per day
    sleep_deficit_per_day = 6 - 4

    # Calculate the total sleep deficit for one week
    sleep_deficit_per_week = sleep_deficit_per_day * 7

    result = sleep_deficit_per_week
    return result

print(solution())