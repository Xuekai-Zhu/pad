def solution():
    """Mr. Maximilian has a rental building that he collects rent from every month. The number of units in the building is 100. If the building is 3/4 occupied for a whole year, and each resident of the building pays a rent of $400, calculate the amount of money Mr. Maximilian receives in that year."""
    # Define the number of units in the building
    units_in_building = 100

    # Define the occupancy rate and calculate the number of occupied units
    occupancy_rate = 3/4
    occupied_units = units_in_building * occupancy_rate

    # Calculate the yearly rent revenue
    yearly_revenue = occupied_units * 12 * 400

    # Display the yearly rent revenue
    result = yearly_revenue
    return result

print(solution())