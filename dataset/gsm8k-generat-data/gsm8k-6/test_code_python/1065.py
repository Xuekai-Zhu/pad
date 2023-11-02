def solution():
    # Calculate the weight of John's squat with sleeves and wraps
    squat_with_sleeves = 600 + 30
    squat_with_wraps = 600 + (600*0.25)

    # Calculate the difference in weight between the two
    difference = squat_with_wraps - squat_with_sleeves
    result = difference
    return result

print(solution())