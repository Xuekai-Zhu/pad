def solution():
    # Calculate the total number of stars on the flag
    total_stars = (3 * 8) + (2 * 6)

    # Calculate the number of 5-star rows
    num_5_stars = 76 - total_stars
    result = num_5_stars
    return result

print(solution())