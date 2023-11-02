def solution():
    pages_per_hour = 10
    pages_per_day_per_person = 5
    num_people = 2
    hours_per_day = pages_per_day_per_person / pages_per_hour
    hours_per_week = hours_per_day * 7 * num_people
    result = hours_per_week
    return result

print(solution())