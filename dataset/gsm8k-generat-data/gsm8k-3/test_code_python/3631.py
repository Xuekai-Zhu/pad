def solution():
    """Codger is a three-footed sloth.  He has a challenging time buying shoes because the stores only sell the shoes in pairs. If he already owns the 3-piece set of shoes he is wearing, how many pairs of shoes does he need to buy to have 5 complete 3-piece sets of shoes?"""
    # Codger needs 5 sets of shoes, each containing 3 shoes
    total_shoes_needed = 5 * 3

    # Codger already has 3 shoes
    shoes_already_owned = 3

    # Each pair of shoes contains 2 shoes
    shoes_per_pair = 2

    # Codger needs to buy additional pairs of shoes to have enough for 5 complete sets
    pairs_of_shoes_needed = (total_shoes_needed - shoes_already_owned) / shoes_per_pair

    # Display the number of pairs of shoes Codger needs to buy
    result = pairs_of_shoes_needed
    return result

print(solution())