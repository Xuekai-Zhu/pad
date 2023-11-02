def solution():
    # Define the variables
    total_units = 100
    occupancy_rate = 3/4
    rent_per_unit = 400

    # Calculate the number of occupied units
    occupied_units = total_units * occupancy_rate

    # Calculate the total rent collected in a year
    total_rent = occupied_units * rent_per_unit * 12

    result = total_rent
    return result

print(solution())