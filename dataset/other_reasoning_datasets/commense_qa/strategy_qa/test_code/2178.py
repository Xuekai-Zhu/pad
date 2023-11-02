def solution():
    avg_family_size = 3
    adam_sandler_bedrooms = 14
    adam_sandler_bathrooms = 7
    # Calculate the number of rooms per person
    rooms_per_person = (adam_sandler_bedrooms + adam_sandler_bathrooms) / avg_family_size
    if rooms_per_person < 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())