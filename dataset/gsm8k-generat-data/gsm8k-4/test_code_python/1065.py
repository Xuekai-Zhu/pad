def solution():
    """John has a raw squat of 600 pounds without sleeves or wraps. Sleeves add 30 pounds to his lift. Wraps add 25% to his squat. How much more pounds does he get out of wraps versus sleeves."""
    # Define John's raw squat
    raw_squat = 600

    # Define the additional weight from sleeves
    sleeves_weight = 30

    # Calculate the weight with sleeves
    squat_with_sleeves = raw_squat + sleeves_weight

    # Define the additional weight from wraps
    wraps_weight = raw_squat * 0.25

    # Calculate the weight with wraps
    squat_with_wraps = raw_squat + wraps_weight

    # Calculate the difference between the weight with wraps and the weight with sleeves
    weight_difference = squat_with_wraps - squat_with_sleeves

    # Return the result
    result = weight_difference
    return result

print(solution())