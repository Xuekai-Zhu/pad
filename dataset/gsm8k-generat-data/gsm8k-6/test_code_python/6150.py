def solution():
    # Calculate the total number of weeks in 4 months
    total_weeks = 4 * 4  # 4 months = 16 weeks

    # Calculate the total growth of the tree in centimeters
    growth_in_cm = (total_weeks // 2) * 50  # the tree grows at a rate of 50 centimeters every 2 weeks

    # Calculate the final height of the tree in centimeters
    final_height_in_cm = (2 * 100) + growth_in_cm  # 1 meter = 100 centimeters

    result = final_height_in_cm
    return result

print(solution())