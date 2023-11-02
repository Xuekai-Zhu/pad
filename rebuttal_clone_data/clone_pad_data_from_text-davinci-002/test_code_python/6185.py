def solution():
    refrigerators_per_hour = 90
    coolers_per_hour = refrigerators_per_hour + 70
    hours_per_day = 9
    days = 5
    refrigerators_total = refrigerators_per_hour * hours_per_day * days
    coolers_total = coolers_per_hour * hours_per_day * days
    result = refrigerators_total + coolers_total
    return result

print(solution())