def solution():
    units = 100  # The number of units in the building is 100
    occupancy_rate = 3 / 4  # The building is 3/4 occupied
    rent_per_unit = 400  # Each resident pays a rent of $400 per month
    months_in_year = 12  # There are 12 months in a year

    # Calculate the total rent collected in a year
    total_rent = units * occupancy_rate * rent_per_unit * months_in_year
    result = total_rent
    return result

print(solution())