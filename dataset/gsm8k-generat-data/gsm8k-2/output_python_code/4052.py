def solution():
    """Seymour runs a plant shop. He has 4 flats of petunias with 8 petunias per flat, 3 flats of roses with 6 roses per flat, and two Venus flytraps. Each petunia needs 8 ounces of fertilizer, each rose needs 3 ounces of fertilizer, and each Venus flytrap needs 2 ounces of fertilizer. How many ounces of fertilizer does Seymour need in total?"""
    petunias = 4 * 8
    roses = 3 * 6
    venus_flytraps = 2
    petunia_fertilizer = petunias * 8
    rose_fertilizer = roses * 3
    venus_flytrap_fertilizer = venus_flytraps * 2
    total_fertilizer = petunia_fertilizer + rose_fertilizer + venus_flytrap_fertilizer
    result = total_fertilizer
    return result

print(solution())