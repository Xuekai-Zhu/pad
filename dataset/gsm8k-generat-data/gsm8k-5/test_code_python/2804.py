def solution():
    onions_per_pot = 4  # Trent chops 4 onions per pot of soup
    tears_per_onion = 2/3  # Trent cries 2 tears for every 3 onions he chops
    pots_of_soup = 6  # Trent is making 6 pots of soup

    # Calculate the total number of onions Trent will chop
    total_onions = onions_per_pot * pots_of_soup

    # Calculate the total number of tears Trent will cry
    total_tears = total_onions * tears_per_onion
    result = total_tears
    return result

print(solution())