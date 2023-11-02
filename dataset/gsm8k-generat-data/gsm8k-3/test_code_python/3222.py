def solution():
    """Nicole collected 400 Pokemon cards. Cindy collected twice as many, and Rex collected half of Nicole and Cindy's combined total. If Rex divided his card equally among himself and his three younger siblings, how many cards does Rex have left?"""
    # Calculate the number of cards Cindy has
    cindy_cards = 2 * 400

    # Calculate the combined number of cards Nicole and Cindy have
    combined_cards = 400 + cindy_cards

    # Calculate the number of cards Rex has
    rex_cards = combined_cards / 2

    # Calculate the total number of cards after Rex shares with his younger siblings
    total_cards = rex_cards / 4

    # Calculate the number of cards Rex has left
    remaining_cards = rex_cards % 4

    # Display the number of cards Rex has left
    result = remaining_cards
    return result

print(solution())