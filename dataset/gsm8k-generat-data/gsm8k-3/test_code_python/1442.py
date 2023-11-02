def solution():
    """Jame is trying to learn to tear playing cards.  He can tear 30 cards at a time.  A new deck of cards has 55 cards if you include the jokers and blank cards.  He tears cards 3 times a week.  If he buys 18 decks how many weeks can he go?"""
    # Define the number of cards in a deck
    CARDS_PER_DECK = 55

    # Define the number of cards Jame can tear at a time
    TEAR_SIZE = 30

    # Define the number of times Jame tears cards per week
    TEAR_PER_WEEK = 3

    # Define the number of decks Jame buys
    NUM_DECKS = 18

    # Calculate the total number of cards Jame has
    total_cards = NUM_DECKS * CARDS_PER_DECK

    # Calculate the number of tears Jame needs to make to tear all the cards
    num_tears = total_cards // TEAR_SIZE
    if total_cards % TEAR_SIZE != 0:
        num_tears += 1

    # Calculate the number of weeks Jame can go tearing cards
    num_weeks = num_tears // TEAR_PER_WEEK
    if num_tears % TEAR_PER_WEEK != 0:
        num_weeks += 1

    # Display the number of weeks Jame can go tearing cards
    result = num_weeks
    return result

print(solution())