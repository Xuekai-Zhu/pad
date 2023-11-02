def solution():
    """Reina has three times the number of counters and four times the number of marbles as Kevin. If Kevin has 40 counters and 50 marbles, calculate the number of counters and marbles that Reina has?"""
    kevin_counters = 40
    kevin_marbles = 50
    reina_counters = 3 * kevin_counters
    reina_marbles = 4 * kevin_marbles
    result = (reina_counters, reina_marbles)
    return result

print(solution())