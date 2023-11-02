def solution():
    initial_speed = 80
    training_weeks = 16
    speed_increase = 0.20  # 20% increase

    # Calculate the final speed after training
    final_speed = initial_speed + (initial_speed * speed_increase)

    # Calculate the average speed gained per week
    speed_gained_per_week = (final_speed - initial_speed) / training_weeks
    result = speed_gained_per_week
    return result

print(solution())