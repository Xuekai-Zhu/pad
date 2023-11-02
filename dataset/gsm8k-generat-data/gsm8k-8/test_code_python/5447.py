def solution():
    # Calculate the time it takes for the water to boil
    boiling_time = (212 - 41) / 3

    # Calculate the total cooking time
    cooking_time = boiling_time + 12 + (1/3 * 12)

    result = cooking_time
    return result

print(solution())