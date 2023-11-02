def solution():
    travel_time_to_work = 5 + 20 + 5
    travel_time_from_work = 5 + 20 + 5
    work_days_per_year = 365
    total_travel_time = (travel_time_to_work + travel_time_from_work) * work_days_per_year
    result = total_travel_time / 60 / 60
    return result

print(solution())