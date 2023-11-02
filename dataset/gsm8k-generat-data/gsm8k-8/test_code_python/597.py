def solution():
    # Calculate total number of cards before throwing any away
    total_cards = (3.5 * 52) + (3 * 52)

    # Subtract the 34 cards that were thrown away
    total_cards -= 34

    result = total_cards
    return result

print(solution())