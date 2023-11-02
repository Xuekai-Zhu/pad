def solution():
    # Calculate the growth rate of the tree each week
    growth_per_week = 50 / 2

    # Calculate the total number of weeks in four months
    total_weeks = 4 * 4

    # Calculate the total growth of the tree in centimeters
    total_growth = growth_per_week * total_weeks

    # Convert the current height of the tree to centimeters
    current_height = 2 * 100

    # Calculate the final height of the tree in centimeters
    final_height = current_height + total_growth
    result = final_height
    return result

print(solution())