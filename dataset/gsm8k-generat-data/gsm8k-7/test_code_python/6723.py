def solution():
    initial_length = 6
    current_length = 36
    growth_rate = 0.5  # in inches per month

    # Calculate the total growth in inches
    total_growth = current_length - initial_length

    # Calculate the total time taken in months
    time_in_months = total_growth / growth_rate

    # Convert the time in months to years
    time_in_years = time_in_months / 12
    result = time_in_years
    return result

print(solution())