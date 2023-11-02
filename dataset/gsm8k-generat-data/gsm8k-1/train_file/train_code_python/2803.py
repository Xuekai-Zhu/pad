def solution():
    """Trent cries 2 tears for every three onions he chops. He needs to chop 4 onions per pot of soup. If he's making 6 pots of soup, how many tears does he cry?"""
    onions_per_pot = 4
    pots_of_soup = 6
    onions_chopped = onions_per_pot * pots_of_soup
    tears_per_onion = 2/3
    total_tears = onions_chopped * tears_per_onion
    result = total_tears
    return result

print(solution())