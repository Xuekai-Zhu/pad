def solution():
    
    total_cards = 80
    a_cards = (2/5) * total_cards
    remaining_cards = total_cards - a_cards
    b_cards = (1/2) * remaining_cards
    remaining_cards -= b_cards
    c_cards = (5/8) * remaining_cards
    d_cards = remaining_cards - c_cards
    result = d_cards
    return result

print(solution())