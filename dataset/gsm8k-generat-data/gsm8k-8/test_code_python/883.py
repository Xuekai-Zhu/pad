def solution():
    # Calculate the total number of bolts
    total_bolts = 7 * 11

    # Calculate the total number of nuts
    total_nuts = 3 * 15

    # Calculate the number of bolts and nuts used in the project
    bolts_used = total_bolts - 3
    nuts_used = total_nuts - 6

    result = (bolts_used, nuts_used)
    return result

print(solution())