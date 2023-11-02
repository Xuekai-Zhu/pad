def solution():
    num_ferns = 3
    num_palms = 5
    num_succulents = 7
    total_plants = 24

    # Calculate the total number of plants Justice already has
    total_current_plants = num_ferns + num_palms + num_succulents

    # Calculate the number of additional plants Justice needs
    additional_plants_needed = total_plants - total_current_plants
    result = additional_plants_needed
    return result

print(solution())