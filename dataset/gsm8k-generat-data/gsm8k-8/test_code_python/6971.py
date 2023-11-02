def solution():
    # Number of hockey cards
    hockey_cards = 200

    # Number of football cards
    football_cards = 4 * hockey_cards

    # Number of baseball cards
    baseball_cards = football_cards - 50

    # Total number of cards
    total_cards = hockey_cards + football_cards + baseball_cards
    result = total_cards
    return result

print(solution())