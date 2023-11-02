def solution():
    # The number of ferns, palms, and succulent plants Justice currently has
    num_ferns = 3
    num_palms = 5
    num_succulents = 7

    # The total number of plants Justice wants
    total_plants = 24

    # Calculate the number of plants Justice needs to reach her goal
    plants_needed = total_plants - (num_ferns + num_palms + num_succulents)

    result = plants_needed
    return result

print(solution())