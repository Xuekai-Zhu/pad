def solution():
    # Convert 18 inches to feet
    space_per_seed = 18 / 12

    # Calculate how many seeds can fit in one row
    seeds_per_row = int(120 / space_per_seed)

    result = seeds_per_row
    return result

print(solution())