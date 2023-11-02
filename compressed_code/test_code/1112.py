def solution():
    
    cards_per_deck = 55
    cards_per_session = 30
    sessions_per_week = 3
    decks_purchased = 18
    total_cards = cards_per_deck * decks_purchased
    total_sessions = total_cards / cards_per_session
    total_weeks = total_sessions / sessions_per_week
    result = total_weeks
    return result

print(solution())