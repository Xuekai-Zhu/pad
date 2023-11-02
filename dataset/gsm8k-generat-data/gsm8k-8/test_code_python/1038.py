def solution():
    # Calculate the number of seeds that grew into plants
    remaining_seeds = 23 - 5
    plants_grew = remaining_seeds / 3

    # Calculate the number of plants that were not eaten by squirrels or rabbits
    uneaten_plants = plants_grew - (plants_grew / 3)

    # Calculate the number of plants Marge ended up with
    plants_end = uneaten_plants - 1  # subtract the weed she pulled and did not keep

    result = plants_end
    return result

print(solution())