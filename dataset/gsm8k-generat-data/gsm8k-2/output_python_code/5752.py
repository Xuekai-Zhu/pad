def solution():
    """There are 55 people at the track meet. 30 of them are boys, and the rest are girls. Three fifths of the girls have long hair, and the rest have short hair. How many girls have short hair?"""
    total_people = 55
    boys = 30
    girls = total_people - boys
    long_hair = (3/5) * girls
    short_hair = girls - long_hair
    result = short_hair
    return result

print(solution())