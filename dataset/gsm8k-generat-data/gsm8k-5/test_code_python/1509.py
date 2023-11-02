def solution():
    initial_height_inches = 66  # John was initially 66 inches tall
    growth_rate_inches_per_month = 2  # John grew 2 inches per month for 3 months
    growth_period_months = 3

    # Calculate John's final height in inches
    final_height_inches = initial_height_inches + (growth_rate_inches_per_month * growth_period_months)

    # Convert John's height to feet
    height_feet = final_height_inches / 12
    result = height_feet
    return result

print(solution())