def solution():
    # Calculate James' new powerlifting total after gaining 15%
    total_before = 2200
    percent_gain = 0.15
    total_after = total_before + (total_before * percent_gain)

    # Calculate James' new body weight after gaining 8 pounds
    weight_before = 245
    weight_after = weight_before + 8

    # Calculate the ratio of lifting total to body weight
    ratio = total_after / weight_after
    result = ratio
    return result

print(solution())