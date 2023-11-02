def solution():
    onion_to_tear_ratio = 3 / 2
    onions_per_pot = 4
    pots_of_soup = 6

    # Calculate the total number of onions Trent needs to chop
    total_onions = onions_per_pot * pots_of_soup

    # Calculate the total number of tears Trent will cry
    total_tears = total_onions * onion_to_tear_ratio
    result = total_tears
    return result

print(solution())