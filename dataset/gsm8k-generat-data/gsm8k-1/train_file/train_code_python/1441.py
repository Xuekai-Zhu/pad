def solution():
    """Jame is trying to learn to tear playing cards. He can tear 30 cards at a time. A new deck of cards has 55 cards if you include the jokers and blank cards. He tears cards 3 times a week. If he buys 18 decks how many weeks can he go?"""
    cards_torn_per_session = 30
    decks_bought = 18
    cards_per_deck = 55
    total_cards = decks_bought * cards_per_deck
    sessions_per_week = 3
    weeks = total_cards / (cards_torn_per_session * sessions_per_week)
    result = weeks
    return result

print(solution())