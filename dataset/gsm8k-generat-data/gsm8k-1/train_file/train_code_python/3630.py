def solution():
    """Codger is a three-footed sloth. He has a challenging time buying shoes because the stores only sell the shoes in pairs. 
    If he already owns the 3-piece set of shoes he is wearing, how many pairs of shoes does he need to buy to have 5 complete 3-piece sets of shoes?"""
    shoes_per_set = 3
    sets_needed = 5
    total_shoes_needed = (sets_needed * shoes_per_set) - 3  # Subtract the shoes already owned
    pairs_needed = (total_shoes_needed + 1) // 2  # Add one to round up to the nearest pair
    result = pairs_needed
    return result

print(solution())