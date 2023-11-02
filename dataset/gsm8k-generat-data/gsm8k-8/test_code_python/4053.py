def solution():
    # Calculate the total number of petunias
    petunia_count = 4 * 8

    # Calculate the total number of roses
    rose_count = 3 * 6

    # Calculate the total number of Venus flytraps
    flytrap_count = 2

    # Calculate the total amount of fertilizer needed for the petunias
    petunia_fertilizer = petunia_count * 8

    # Calculate the total amount of fertilizer needed for the roses
    rose_fertilizer = rose_count * 3

    # Calculate the total amount of fertilizer needed for the Venus flytraps
    flytrap_fertilizer = flytrap_count * 2

    # Calculate the total amount of fertilizer needed
    total_fertilizer = petunia_fertilizer + rose_fertilizer + flytrap_fertilizer

    result = total_fertilizer
    return result

print(solution())