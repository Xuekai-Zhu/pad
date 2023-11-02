def solution():
    # Calculate the number of girls at the track meet
    total_people = 55
    boys = 30
    girls = total_people - boys

    # Calculate the number of girls with long hair
    long_hair_girls = (3/5) * girls

    # Calculate the number of girls with short hair
    short_hair_girls = girls - long_hair_girls
    result = short_hair_girls
    return result

print(solution())