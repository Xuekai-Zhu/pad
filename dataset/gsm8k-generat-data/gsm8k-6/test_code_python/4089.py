def solution():
    # Find Benjy's number of peaches
    benjy_peaches = (16 - 6) / 2  # Martine has 6 more than twice as many peaches as Benjy

    # Find Gabrielle's number of peaches
    gabrielle_peaches = benjy_peaches * 3  # Benjy has one-third as many peaches as Gabrielle

    result = gabrielle_peaches
    return result

print(solution())