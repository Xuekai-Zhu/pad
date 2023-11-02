def solution():
    """It takes a butterfly egg 120 days to become a butterfly. If each butterfly spends 3 times as much time as a larva as in a cocoon, how long does each butterfly spend in a cocoon?"""
    total_time = 120
    larva_time = total_time / 4
    cocoon_time = (total_time - larva_time) / 4
    result = cocoon_time
    return result

print(solution())