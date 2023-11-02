def solution():
    # Define initial fastball speed and increase percentage
    initial_speed = 80
    increase_percentage = 0.20

    # Calculate final fastball speed after training
    final_speed = initial_speed * (1 + increase_percentage)

    # Calculate total number of training weeks
    total_weeks = 4 * 4

    # Calculate speed gained per week
    speed_gained_per_week = (final_speed - initial_speed) / total_weeks

    result = speed_gained_per_week
    return result

print(solution())