def solution():
    """Trent cries 2 tears for every three onions he chops. He needs to chop 4 onions per pot of soup. If he's making 6 pots of soup, how many tears does he cry?"""
    onions_per_pot = 4
    total_pots = 6
    tears_per_onion = 2 / 3
    total_onions = onions_per_pot * total_pots
    total_tears = (total_onions * tears_per_onion) * 2
    result = total_tears
    return result

print(solution())