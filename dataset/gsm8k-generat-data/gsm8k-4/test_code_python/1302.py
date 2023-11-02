def solution():
    """Reina has three times the number of counters and four times the number of marbles as Kevin. If Kevin has 40 counters and 50 marbles, calculate the number of counters and marbles that Reina has?"""
    # Define Kevin's number of counters and marbles
    kevin_counters = 40
    kevin_marbles = 50

    # Calculate Reina's number of counters and marbles
    reina_counters = kevin_counters * 3
    reina_marbles = kevin_marbles * 4

    # Return the result
    result = (reina_counters, reina_marbles)
    return result

print(solution())