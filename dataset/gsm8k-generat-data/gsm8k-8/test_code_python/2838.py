def solution():
    # Convert Esther's distance to feet
    esther_distance = 975 / 3

    # Convert Niklaus's distance to feet
    niklaus_distance = 1287 / 3

    # Convert Lionel's distance to feet
    lionel_distance = 4 * 5280

    # Calculate the total distance in feet
    total_distance = lionel_distance + esther_distance + niklaus_distance
    result = total_distance
    return result

print(solution())