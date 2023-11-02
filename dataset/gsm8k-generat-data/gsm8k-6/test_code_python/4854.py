def solution():
    # Calculate the speed at which Jed was traveling
    speed_over_limit = 256 / 16  # Jed was fined $16 for each mile per hour he was over the speed limit
    jed_speed = 50 + speed_over_limit  # Jed's speed is the speed limit plus the speed he was over the limit
    result = jed_speed
    return result

print(solution())