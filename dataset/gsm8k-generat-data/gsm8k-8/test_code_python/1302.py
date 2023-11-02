def solution():
    # Define Kevin's counters and marbles
    kevin_counters = 40
    kevin_marbles = 50

    # Calculate Reina's counters and marbles
    reina_counters = 3 * kevin_counters
    reina_marbles = 4 * kevin_marbles

    result = (reina_counters, reina_marbles)
    return result

print(solution())