def solution():
    total_people = 55
    num_boys = 30
    num_girls = total_people - num_boys

    # Calculate the number of girls with long hair
    girls_long_hair = (3/5) * num_girls

    # Calculate the number of girls with short hair
    girls_short_hair = num_girls - girls_long_hair

    result = girls_short_hair
    return result

print(solution())