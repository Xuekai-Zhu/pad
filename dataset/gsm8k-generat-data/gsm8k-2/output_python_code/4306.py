def solution():
    """Mr. Maximilian has a rental building that he collects rent from every month. The number of units in the building is 100. If the building is 3/4 occupied for a whole year, and each resident of the building pays a rent of $400, calculate the amount of money Mr. Maximilian receives in that year."""
    total_units = 100
    occupied_units = total_units * 0.75
    rent_per_unit = 400
    total_rent_per_month = occupied_units * rent_per_unit
    total_rent_per_year = total_rent_per_month * 12
    result = total_rent_per_year
    return result

print(solution())