def solution():
    """Seymour runs a plant shop. He has 4 flats of petunias with 8 petunias per flat, 
    3 flats of roses with 6 roses per flat, and two Venus flytraps. Each petunia needs 
    8 ounces of fertilizer, each rose needs 3 ounces of fertilizer, and each Venus flytrap 
    needs 2 ounces of fertilizer. How many ounces of fertilizer does Seymour need in total?"""
    # Calculate the total number of petunias
    petunias = 4 * 8

    # Calculate the total number of roses
    roses = 3 * 6

    # Calculate the total number of Venus flytraps
    flytraps = 2

    # Calculate the total amount of fertilizer needed for petunias
    petunia_fertilizer = petunias * 8

    # Calculate the total amount of fertilizer needed for roses
    rose_fertilizer = roses * 3

    # Calculate the total amount of fertilizer needed for Venus flytraps
    flytrap_fertilizer = flytraps * 2

    # Calculate the total amount of fertilizer needed
    total_fertilizer = petunia_fertilizer + rose_fertilizer + flytrap_fertilizer

    # return the result
    result = total_fertilizer
    return result

print(solution())