def solution():
    
    cards_torn_per_session = 30
    decks_bought = 18
    cards_per_deck = 55
    total_cards = decks_bought * cards_per_deck
    sessions_per_week = 3
    weeks = total_cards / (cards_torn_per_session * sessions_per_week)
    result = weeks
    return result

print(solution())