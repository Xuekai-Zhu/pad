def solution():
    orlando_gain = 5  # Orlando gained 5 pounds
    jose_gain = 2 + 2 * orlando_gain  # Jose gained 2 pounds more than twice what Orlando gained
    fernando_gain = (1/2) * jose_gain - 3  # Fernando gained 3 pounds less than half of what Jose gained

    # Calculate the total weight the three family members gained
    total_gain = orlando_gain + jose_gain + fernando_gain
    result = total_gain
    return result

print(solution())