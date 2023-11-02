def solution():
    petunias_per_flat = 8
    num_petunia_flats = 4
    roses_per_flat = 6
    num_rose_flats = 3
    num_vft = 2

    fertilizer_per_petunia = 8
    fertilizer_per_rose = 3
    fertilizer_per_vft = 2

    total_petunias = petunias_per_flat * num_petunia_flats
    total_roses = roses_per_flat * num_rose_flats
    total_vft = num_vft

    total_fertilizer = (total_petunias * fertilizer_per_petunia) + (total_roses * fertilizer_per_rose) + (total_vft * fertilizer_per_vft)
    result = total_fertilizer
    return result

print(solution())