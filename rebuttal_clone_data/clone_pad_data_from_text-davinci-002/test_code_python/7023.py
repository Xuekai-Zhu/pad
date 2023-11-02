def solution():
    miles_run_per_day = [3, 4, 6, 8, 3]
    pace_per_mile = 10
    total_hours = 0
    for miles in miles_run_per_day:
        hours = miles * pace_per_mile
        total_hours += hours
    result = total_hours
    return result

print(solution())