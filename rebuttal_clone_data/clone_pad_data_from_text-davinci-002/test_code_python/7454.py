def solution():
    dogs = 2
    minutes_per_dog = 20
    days = 30
    hours_per_day = 24
    total_hours = (dogs * minutes_per_dog * days) / hours_per_day
    result = total_hours
    return result

print(solution())