def solution():
    
    minutes_per_dog = 20
    dogs = 2
    days = 30
    minutes_per_day = minutes_per_dog * dogs
    total_minutes = minutes_per_day * days
    hours = total_minutes / 60
    result = hours
    return result

print(solution())