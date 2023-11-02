def solution():
    """Codger is a three-footed sloth. He has a challenging time buying shoes because the stores only sell the shoes in pairs. If he already owns the 3-piece set of shoes he is wearing, how many pairs of shoes does he need to buy to have 5 complete 3-piece sets of shoes?"""
    current_sets = 1  # Codger already owns one set
    needed_sets = 5
    pairs_needed = (needed_sets * 3 - 3) // 2  # Subtract 3 for Codger's own shoes, divide by 2 for pairs
    result = pairs_needed
    return result

print(solution())