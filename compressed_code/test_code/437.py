def solution():
    
    full_decks = 3
    half_full_decks = 3
    total_cards = (full_decks * 52) + (half_full_decks * 26)
    cards_thrown_away = 34
    remaining_cards = total_cards - cards_thrown_away
    result = remaining_cards
    return result

print(solution())