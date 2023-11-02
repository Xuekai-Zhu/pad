def solution():
    """Codger is a three-footed sloth. He has a challenging time buying shoes because the stores only sell the shoes in pairs. If he already owns the 3-piece set of shoes he is wearing, how many pairs of shoes does he need to buy to have 5 complete 3-piece sets of shoes?"""
    # Define the number of 3-piece sets of shoes Codger wants to have
    sets_wanted = 5

    # Define the number of feet on each set of shoes Codger needs
    feet_per_set = 3

    # Define the number of feet Codger already has shoes for
    feet_owned = 3

    # Calculate the number of feet Codger needs shoes for
    feet_needed = feet_per_set * sets_wanted - feet_owned

    # Calculate the number of pairs of shoes Codger needs to buy
    pairs_needed = feet_needed // 2

    # return the result
    result = pairs_needed
    return result

print(solution())