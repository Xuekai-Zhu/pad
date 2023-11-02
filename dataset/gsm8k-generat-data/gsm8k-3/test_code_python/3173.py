def solution():
    """Phil likes to collect baseball cards.  He buys a pack of twenty each week for a year, but then loses half of them one day in a fire.  How many baseball cards does Phil have left?"""
    # Define the number of weeks in a year and the number of cards in a pack
    WEEKS_IN_YEAR = 52
    CARDS_PER_PACK = 20

    # Calculate the total number of cards before the fire
    total_cards = WEEKS_IN_YEAR * CARDS_PER_PACK

    # Calculate the number of cards that Phil has left after the fire
    cards_left = total_cards / 2

    # Display the number of cards Phil has left
    result = cards_left
    return result

print(solution())