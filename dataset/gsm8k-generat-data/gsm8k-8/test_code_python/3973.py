def solution():
    # Define Jenny's number of cards
    jenny_cards = 6

    # Calculate Orlando's number of cards
    orlando_cards = jenny_cards + 2

    # Calculate Richard's number of cards
    richard_cards = 3 * orlando_cards

    # Calculate the total number of cards
    total_cards = jenny_cards + orlando_cards + richard_cards

    result = total_cards
    return result

print(solution())