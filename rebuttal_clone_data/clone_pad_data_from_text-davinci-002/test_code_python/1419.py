def solution():
    total_kilometers = 20
    first_day = 2
    day = 5
    daily_increase = 1
    fifth_day = first_day + (daily_increase * (day - 1))
    result = fifth_day
    return result

print(solution())