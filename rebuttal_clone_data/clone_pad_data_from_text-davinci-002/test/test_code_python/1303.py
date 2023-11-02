def solution():
    minutes_per_short_hair = 10
    minutes_per_full_hair = minutes_per_short_hair * 2
    short_hair_dogs = 6
    full_hair_dogs = 9
    total_dogs = short_hair_dogs + full_hair_dogs
    total_minutes = (short_hair_dogs * minutes_per_short_hair) + (full_hair_dogs * minutes_per_full_hair)
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())