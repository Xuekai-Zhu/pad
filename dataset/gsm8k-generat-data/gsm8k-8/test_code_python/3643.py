def solution():
    # Calculate the total number of chairs for indoor tables
    indoor_chairs = 8 * 3

    # Calculate the total number of chairs for outdoor tables
    outdoor_chairs = 12 * 3

    # Calculate the total number of chairs in the bakery
    total_chairs = indoor_chairs + outdoor_chairs

    result = total_chairs
    return result

print(solution())