def solution():
    # Calculate the total increase in speed
    initial_speed = 80  # miles per hour
    final_speed = initial_speed * 1.2
    total_increase = final_speed - initial_speed

    # Calculate the increase in speed per week
    weeks = 4 * 4  # 4 training sessions each lasting 4 weeks
    increase_per_week = total_increase / weeks
    result = increase_per_week
    return result

print(solution())