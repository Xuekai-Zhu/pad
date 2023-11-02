def solution():
    """It takes a butterfly egg 120 days to become a butterfly. If each butterfly spends 3 times as much time as a larva as in a cocoon, how long does each butterfly spend in a cocoon?"""
    # Define the total lifecycle of a butterfly
    total_lifecycle = 120

    # Define the ratio of time spent as a larva to time spent in a cocoon
    larva_to_cocoon_ratio = 3

    # Calculate the time spent in a cocoon
    cocoon_time = total_lifecycle / (larva_to_cocoon_ratio + 1)

    # Display the time spent in a cocoon
    result = cocoon_time
    return result

print(solution())