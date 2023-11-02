def solution():
    raw_squat = 600
    sleeves_add = 30
    wraps_add_percent = 0.25

    # Calculate the squat with sleeves
    squat_with_sleeves = raw_squat + sleeves_add

    # Calculate the additional pounds from wraps
    wrap_added_pounds = raw_squat * wraps_add_percent

    # Calculate the squat with wraps
    squat_with_wraps = raw_squat + wrap_added_pounds

    # Calculate the additional pounds from wraps compared to sleeves
    additional_pounds_from_wraps = squat_with_wraps - squat_with_sleeves
    result = additional_pounds_from_wraps
    return result

print(solution())