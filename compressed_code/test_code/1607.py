def solution():
    
    initial_cards = 4 + 13 + 36
    bad_cards = 4
    remaining_cards = initial_cards - bad_cards - 29
    result = remaining_cards
    return result

print(solution())