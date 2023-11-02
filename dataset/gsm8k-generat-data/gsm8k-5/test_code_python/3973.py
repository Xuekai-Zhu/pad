def solution():
    jenny_cards = 6  # Jenny has 6 cards
    orlando_cards = jenny_cards + 2  # Orlando has 2 more cards than Jenny
    richard_cards = orlando_cards * 3  # Richard has three times as many cards as Orlando

    # Calculate the total number of cards
    total_cards = jenny_cards + orlando_cards + richard_cards
    result = total_cards
    return result

print(solution())