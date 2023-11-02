def solution():
    total_acres = 1700  # Farmer Randy needs to plant 1700 acres of cotton
    total_days = 5  # Farmer Randy has 5 days to plant the cotton
    tractors_1 = 2  # Two tractors work for the first 2 days
    tractors_2 = 7  # Seven tractors work for the next 3 days

    # Calculate the total number of tractor-days
    tractor_days = (tractors_1 * 2) + (tractors_2 * 3)

    # Calculate the number of acres each tractor needs to plant per day
    acres_per_day = total_acres / tractor_days
    result = acres_per_day
    return result

print(solution())