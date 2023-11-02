def solution():
    
    onions_per_pot = 4
    pots_of_soup = 6
    onions_chopped = onions_per_pot * pots_of_soup
    tears_per_onion = 2/3
    total_tears = onions_chopped * tears_per_onion
    result = total_tears
    return result

print(solution())