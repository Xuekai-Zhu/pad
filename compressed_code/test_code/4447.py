def solution():
    
    total_people = 55
    boys = 30
    girls = total_people - boys
    long_hair = (3/5) * girls
    short_hair = girls - long_hair
    result = short_hair
    return result

print(solution())