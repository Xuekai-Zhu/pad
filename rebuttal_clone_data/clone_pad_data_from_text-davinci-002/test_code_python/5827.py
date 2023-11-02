def solution():
    pages_ryan = 2100
    pages_brother = 200
    days = 7
    pages_per_day_ryan = pages_ryan / days
    pages_per_day_brother = pages_brother / days
    result = pages_per_day_ryan - pages_per_day_brother
    
    return result

print(solution())