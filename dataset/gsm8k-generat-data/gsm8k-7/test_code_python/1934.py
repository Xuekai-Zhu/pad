def solution():
    initial_rent = 300
    increased_rent = 350
    num_initial_years = 3
    num_total_years = 5

    # Calculate the total cost for the initial 3 years
    total_initial_cost = initial_rent * 12 * num_initial_years

    # Calculate the total cost for the remaining 2 years at the increased rate
    total_remaining_cost = increased_rent * 12 * (num_total_years - num_initial_years)

    # Calculate the total cost for the entire 5-year period
    total_cost = total_initial_cost + total_remaining_cost
    result = total_cost
    return result

print(solution())