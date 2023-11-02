def solution():
    initial_height = 66 # inches
    growth_rate = 2 # inches per month
    num_months = 3

    # Calculate John's final height in inches
    final_height = initial_height + (growth_rate * num_months)

    # Convert final height to feet
    final_height_feet = final_height / 12

    result = final_height_feet
    return result

print(solution())