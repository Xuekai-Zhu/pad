def solution():
    num_rows = 7
    num_plants_per_row = 18
    extra_plants = 15

    # Calculate the total number of plants that Papi Calot initially planned to plant
    planned_plants = num_rows * num_plants_per_row

    # Calculate the total number of plants with the additional 15 plants
    total_plants = planned_plants + extra_plants
    result = total_plants
    return result

print(solution())