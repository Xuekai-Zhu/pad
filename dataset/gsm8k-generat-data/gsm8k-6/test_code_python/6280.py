def solution():
    # Find the total number of cheese sticks
    total_sticks = 15 + 30 + 45

    # Find the number of pepperjack sticks
    pepperjack_sticks = 45

    # Calculate the percentage chance of picking a pepperjack stick
    chance_pepperjack = (pepperjack_sticks / total_sticks) * 100
    result = chance_pepperjack
    return result

print(solution())