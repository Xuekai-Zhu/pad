def solution():
    """Jame is trying to learn to tear playing cards. He can tear 30 cards at a time. A new deck of cards has 55 cards if you include the jokers and blank cards. He tears cards 3 times a week. If he buys 18 decks how many weeks can he go?"""
    # Define the number of cards Jame can tear at a time
    cards_per_tear = 30

    # Define the number of cards in a new deck
    cards_per_deck = 55

    # Calculate the total number of cards Jame has
    total_cards = cards_per_deck * 18

    # Calculate the number of tears Jame needs to tear all the cards
    total_tears = total_cards // cards_per_tear

    # Calculate the number of weeks it will take Jame to tear all the cards
    weeks = total_tears // 3

    # return the result
    result = weeks
    return result

print(solution())