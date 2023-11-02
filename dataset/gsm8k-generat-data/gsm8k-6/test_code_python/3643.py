def solution():
    # Calculate the total number of chairs
    chairs_indoor = 8 * 3  # each indoor table has 3 chairs
    chairs_outdoor = 12 * 3  # each outdoor table has 3 chairs
    total_chairs = chairs_indoor + chairs_outdoor
    result = total_chairs
    return result

print(solution())