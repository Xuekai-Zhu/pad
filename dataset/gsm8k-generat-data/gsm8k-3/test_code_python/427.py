def solution():
    """Calculate how much money will be in Sheila's piggy bank at the end of 4 years."""

    # Define variables
    initial_savings = 3000
    monthly_savings = 276
    time_in_months = 4 * 12
    one_time_addition = 7000

    # Calculate total savings over 4 years
    total_savings = initial_savings + (monthly_savings * time_in_months) + one_time_addition

    # Display total savings
    result = total_savings
    return result

print(solution())