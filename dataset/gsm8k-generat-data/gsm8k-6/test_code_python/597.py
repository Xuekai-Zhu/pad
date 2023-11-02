def solution():
    # Calculate the total number of cards before throwing away
    cards_before = (3 * 52) + (3 * 26)  # 3 full decks and 3 half-full decks (26 cards each)

    # Calculate the total number of cards after throwing away
    cards_after = cards_before - 34

    result = cards_after
    return result

print(solution())