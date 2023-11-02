def solution():
    """Seymour runs a plant shop. He has 4 flats of petunias with 8 petunias per flat, 3 flats of roses with 6 roses per flat, and two Venus flytraps. Each petunia needs 8 ounces of fertilizer, each rose needs 3 ounces of fertilizer, and each Venus flytrap needs 2 ounces of fertilizer. How many ounces of fertilizer does Seymour need in total?"""
    # Define the number of plants and fertilizer needed per plant
    PETUNIAS_PER_FLAT = 8
    ROSES_PER_FLAT = 6
    VENUS_FLYTRAPS = 2
    FERTILIZER_PER_PETUNIA = 8
    FERTILIZER_PER_ROSE = 3
    FERTILIZER_PER_VENUS_FLYTRAP = 2

    # Define the number of flats and plants of each type Seymour has
    petunia_flats = 4
    rose_flats = 3
    venus_flytraps = 2

    # Calculate the total number of each type of plant
    total_petunias = petunia_flats * PETUNIAS_PER_FLAT
    total_roses = rose_flats * ROSES_PER_FLAT
    total_venus_flytraps = venus_flytraps

    # Calculate the total amount of fertilizer needed
    fertilizer_needed = (total_petunias * FERTILIZER_PER_PETUNIA) + (total_roses * FERTILIZER_PER_ROSE) + (total_venus_flytraps * FERTILIZER_PER_VENUS_FLYTRAP)

    # Display the total amount of fertilizer needed
    result = fertilizer_needed
    return result

print(solution())