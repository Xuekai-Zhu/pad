def solution():
    # Calculate the total ounces of fertilizer needed for petunias
    petunia_fertilizer = 4 * 8 * 8  # 4 flats of petunias with 8 petunias per flat, and each petunia needs 8 ounces of fertilizer

    # Calculate the total ounces of fertilizer needed for roses
    rose_fertilizer = 3 * 6 * 3  # 3 flats of roses with 6 roses per flat, and each rose needs 3 ounces of fertilizer

    # Calculate the total ounces of fertilizer needed for Venus flytraps
    flytrap_fertilizer = 2 * 2  # 2 Venus flytraps, each needing 2 ounces of fertilizer

    # Calculate the total amount of fertilizer needed
    total_fertilizer = petunia_fertilizer + rose_fertilizer + flytrap_fertilizer
    result = total_fertilizer
    return result

print(solution())