def solution():
    # Define Diana's current reading and gaming ratio
    current_ratio = 30 / 60

    # Calculate Diana's current gaming time based on her current reading time
    current_gaming_time = current_ratio * 12 * 60

    # Calculate Diana's new reward percentage and convert it to a fraction
    new_reward_percentage = 20
    new_reward_fraction = (100 + new_reward_percentage) / 100

    # Calculate Diana's new gaming time based on her increased reward percentage
    new_gaming_time = new_reward_fraction * current_gaming_time

    # Calculate the difference between Diana's new and current gaming time
    difference = new_gaming_time - current_gaming_time
    result = difference
    return result

print(solution())