def solution():
    growth_rate = 50  # centimeters every two weeks
    initial_height = 200  # centimeters
    num_months = 4

    # Calculate the total growth in centimeters over four months
    num_weeks = num_months * 4
    total_growth = (num_weeks // 2) * growth_rate

    # Add the initial height to the total growth to get the final height
    final_height = initial_height + total_growth
    result = final_height
    return result

print(solution())