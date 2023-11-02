def solution():
     tears_per_onion = 2/3
     onions_per_pot = 4
     pots_of_soup = 6
     total_onions = onions_per_pot * pots_of_soup
     total_tears = total_onions * tears_per_onion
     result = total_tears
     return result

print(solution())