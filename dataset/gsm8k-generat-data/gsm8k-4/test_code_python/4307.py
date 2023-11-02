def solution():
    """
    Mr. Maximilian has a rental building that he collects rent from every month. 
    The number of units in the building is 100. If the building is 3/4 occupied for a whole year, 
    and each resident of the building pays a rent of $400, calculate the amount of money Mr. Maximilian receives in that year.
    """
    # Define the total units in the building and the occupancy rate
    units = 100
    occupancy_rate = 0.75

    # Calculate the number of occupied units
    occupied_units = units * occupancy_rate

    # Calculate the total rent collected in a month
    rent_per_unit = 400
    total_rent = occupied_units * rent_per_unit

    # Calculate the total rent collected in a year
    total_rent_year = total_rent * 12

    # return the result
    result = total_rent_year
    return result

print(solution())