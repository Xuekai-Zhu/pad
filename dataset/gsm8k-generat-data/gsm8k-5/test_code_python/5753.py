def solution():
    total_people = 55  # There are 55 people at the track meet
    boys = 30  # 30 of them are boys
    girls = total_people - boys  # The rest are girls
    long_hair_girls = (3/5) * girls  # Three fifths of the girls have long hair
    short_hair_girls = girls - long_hair_girls  # The rest have short hair
    result = short_hair_girls
    return result

print(solution())