def solution():
    raw_squat = 600  # John's raw squat is 600 pounds
    sleeves = 30  # Sleeves add 30 pounds to John's lift
    wraps = raw_squat * 0.25  # Wraps add 25% to John's squat
    total_sleeves = raw_squat + sleeves  # Total weight with sleeves
    total_wraps = raw_squat + wraps  # Total weight with wraps

    # Calculate the difference in pounds between wraps and sleeves
    difference = total_wraps - total_sleeves
    result = difference
    return result

print(solution())