def solution():
    lionel_distance = 4  # Lionel walked 4 miles
    esther_distance = 975 / 1760  # Esther walked 975 yards, which is 0.5568 miles
    niklaus_distance = 1287 / 5280  # Niklaus walked 1287 feet, which is 0.24432 miles

    # Convert all distances to feet and add them up
    total_distance = (lionel_distance + esther_distance + niklaus_distance) * 5280

    result = total_distance
    return result

print(solution())