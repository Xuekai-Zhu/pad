def solution():
    num_units = 100
    occupancy_rate = 0.75
    rent_per_unit = 400
    num_months = 12

    # Calculate the total number of occupied units for the whole year
    total_occupied_units = num_units * occupancy_rate

    # Calculate the total amount of rent that Mr. Maximilian collects in a month
    total_monthly_rent = total_occupied_units * rent_per_unit

    # Calculate the total amount of rent that he collects in a year
    total_yearly_rent = total_monthly_rent * num_months
    result = total_yearly_rent
    return result

print(solution())