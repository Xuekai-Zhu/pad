def solution():
    """Mr. Maximilian has a rental building that he collects rent from every month. The number of units in the building is 100. If the building is 3/4 occupied for a whole year, and each resident of the building pays a rent of $400, calculate the amount of money Mr. Maximilian receives in that year."""
    num_units = 100
    occupancy_rate = 3/4
    rent_per_unit = 400
    total_rent_per_month = num_units * occupancy_rate * rent_per_unit
    total_rent_per_year = total_rent_per_month * 12
    result = total_rent_per_year
    return result

print(solution())