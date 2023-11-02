def solution():
    hours_per_day = 6
    num_days = 5
    hours_total = hours_per_day * num_days

    kilowatts_per_hour = 7.2 / 8
    kilowatts_total = kilowatts_per_hour * hours_total
    result = kilowatts_total
    return result

print(solution())