def solution():
    """Jame is trying to learn to tear playing cards. He can tear 30 cards at a time. A new deck of cards has 55 cards if you include the jokers and blank cards. He tears cards 3 times a week. If he buys 18 decks how many weeks can he go?"""
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