def solution():
    # Calculate the total number of bolts and nuts purchased by the builder
    bolts_purchased = 7 * 11
    nuts_purchased = 3 * 15

    # Calculate the total number of bolts and nuts used in the project
    bolts_used = bolts_purchased - 3
    nuts_used = (3 * 15) - 6

    result = (bolts_used, nuts_used)
    return result

print(solution())