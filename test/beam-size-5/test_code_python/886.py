def solution():
    total_plants = 100  # There are 100 plants in Mrs. Smith's garden
    indoor_plants = total_plants / 4  # One-fourth of her plants are indoor plants
    remaining_plants = total_plants - indoor_plants  # Calculate the number of remaining plants
    outdoor_plants = (2/3) * remaining_plants  # Two-thirds of the remaining plants are outdoor plants
    flowering_plants = remaining_plants - outdoor_plants  # The rest are flowering plants

    # Calculate the percentage of flowering plants that are flowering plants
    flowering_percentage = (flowering_plants / total_plants) * 100
    result = flowering_percentage
    return result

print(solution())