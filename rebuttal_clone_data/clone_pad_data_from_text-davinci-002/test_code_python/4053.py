def solution():
     petunia_flats = 4
     petunias_per_flat = 8
     rose_flats = 3
     roses_per_flat = 6
     venus_flytraps = 2
     petunia_fertilizer = petunia_flats * petunias_per_flat * 8
     rose_fertilizer = rose_flats * roses_per_flat * 3
     flytrap_fertilizer = venus_flytraps * 2
     total_fertilizer = petunia_fertilizer + rose_fertilizer + flytrap_fertilizer
     result = total_fertilizer
     return result

print(solution())