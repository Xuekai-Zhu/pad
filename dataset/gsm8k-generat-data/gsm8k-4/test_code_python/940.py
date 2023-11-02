def solution():
    """Lloyd, Mark, and Michael have their Pokemon cards collection. Currently, Mark has thrice as many cards as Lloyd but has 10 fewer cards than Michael. If Michael has 100 cards now, how many more cards should they collect so that all three of them will have a total of 300 cards?"""
    # Define the number of cards currently owned by Michael
    michael_cards = 100

    # Calculate the number of cards owned by Mark and Lloyd
    mark_cards = 3 * lloyd_cards - 10
    lloyd_cards = mark_cards / 3

    # Calculate the total number of cards they currently own
    total_cards = michael_cards + mark_cards + lloyd_cards

    # Calculate the number of cards they need to collect
    cards_needed = 300 - total_cards

    # return the result
    result = cards_needed
    return result

print(solution())