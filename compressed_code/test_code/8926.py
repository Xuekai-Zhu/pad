def solution():
    
    pages_per_hour = 10
    pages_per_person = 5
    people = 2
    pages_per_day = pages_per_person * people
    hours_per_day = pages_per_day / pages_per_hour
    hours_per_week = hours_per_day * 7
    result = hours_per_week
    return result

print(solution())