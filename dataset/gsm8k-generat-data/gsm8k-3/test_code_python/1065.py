def solution():
    """John has a raw squat of 600 pounds without sleeves or wraps.  Sleeves add 30 pounds to his lift.  Wraps add 25% to his squat.  How much more pounds does he get out of wraps versus sleeves."""
    # Define John's raw squat
    raw_squat = 600

    # Calculate his squat with sleeves
    squat_with_sleeves = raw_squat + 30

    # Calculate his squat with wraps
    squat_with_wraps = raw_squat * 1.25

    # Calculate the difference between his squat with wraps and with sleeves
    difference = squat_with_wraps - squat_with_sleeves

    # Display the difference in pounds
    result = difference
    return result

print(solution())