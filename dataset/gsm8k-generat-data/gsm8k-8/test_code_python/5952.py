def solution():
    # Define the weight gained by Orlando
    orlando_gain = 5

    # Define the weight gained by Jose
    jose_gain = 2 + 2*orlando_gain

    # Define the weight gained by Fernando
    fernando_gain = 0.5*jose_gain - 3

    # Calculate the total weight gained by the three family members
    total_gain = orlando_gain + jose_gain + fernando_gain
    result = total_gain
    return result

print(solution())