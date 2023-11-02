def solution():
    rows = 7  # Papi Calot planned to plant 7 rows
    plants_per_row = 18  # He planned to plant 18 plants per row
    additional_plants = 15  # He is thinking about adding 15 more plants

    # Calculate the total number of plants Papi Calot will have after adding the additional plants
    total_plants = rows * plants_per_row + additional_plants
    result = total_plants
    return result

print(solution())