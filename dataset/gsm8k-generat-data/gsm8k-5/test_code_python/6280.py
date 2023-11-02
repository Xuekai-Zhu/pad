def solution():
    total_sticks = 15 + 30 + 45  # The total number of cheese sticks in the pack is 90
    pepperjack_sticks = 45  # There are 45 pepperjack sticks in the pack

    # Calculate the percentage chance that a randomly chosen stick will be pepperjack
    percentage = (pepperjack_sticks / total_sticks) * 100
    result = percentage
    return result

print(solution())