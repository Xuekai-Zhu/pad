def solution():
    # Calculate the total number of dresses sewn by Jane
    total_dresses = 2 * 7 + 3 * 2  # Jane sews 2 dresses a day for 7 days and 3 dresses a day for 2 days

    # Calculate the total number of ribbons used by Jane
    total_ribbons = 2 * total_dresses  # Jane adds 2 ribbons to each dress

    result = total_ribbons
    return result

print(solution())