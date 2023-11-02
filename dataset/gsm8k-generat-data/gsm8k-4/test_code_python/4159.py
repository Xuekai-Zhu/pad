def solution():
    """It takes a butterfly egg 120 days to become a butterfly. If each butterfly spends 3 times as much time as a larva as in a cocoon, how long does each butterfly spend in a cocoon?"""
    # Define the number of days for the complete life cycle of a butterfly
    total_days = 120

    # Define the ratio of time spent in cocoon to time spent as larva
    cocoon_to_larva_ratio = 1/3

    # Calculate the number of days spent in cocoon
    cocoon_days = (total_days / (1 + cocoon_to_larva_ratio)) * cocoon_to_larva_ratio

    # Return the result
    result = cocoon_days
    return result

print(solution())