def solution():
    # Calculate the number of girls at the track meet
    girls = 55 - 30

    # Calculate the number of girls with long hair
    girls_long_hair = (3/5) * girls

    # Calculate the number of girls with short hair
    girls_short_hair = girls - girls_long_hair

    result = girls_short_hair
    return result

print(solution())