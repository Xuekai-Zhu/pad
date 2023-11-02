def solution():
    # Calculate the total amount of fertilizer needed for petunias
    petunia_flats = 4
    petunias_per_flat = 8
    per_pentunia = 8
    total_petunias = petunia_flats * petunias_per_flat
    fertilizer_for_petunias = total_petunias * per_pentunia

    # Calculate the total amount of fertilizer needed for roses
    rose_flats = 3
    roses_per_flat = 6
    per_rose = 3
    total_roses = rose_flats * roses_per_flat
    fertilizer_for_roses = total_roses * per_rose

    # Calculate the total amount of fertilizer needed for Venus flytraps
    venus_flytraps = 2
    per_flytrap = 2
    fertilizer_for_flytraps = venus_flytraps * per_flytrap

    # Calculate the total amount of fertilizer needed
    total_fertilizer = fertilizer_for_petunias + fertilizer_for_roses + fertilizer_for_flytraps
    result = total_fertilizer
    return result

print(solution())