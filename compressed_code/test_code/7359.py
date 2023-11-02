def solution():
    
    total_cards = 120
    red_cards = (2/5) * total_cards
    remaining_cards = total_cards - red_cards
    black_cards = (5/9) * remaining_cards
    green_cards = remaining_cards - black_cards
    result = green_cards
    return result

print(solution())