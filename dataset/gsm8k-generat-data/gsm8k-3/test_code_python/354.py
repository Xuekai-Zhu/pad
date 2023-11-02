def solution():
    """Punger collects baseball cards.  He buys 60 packs of baseball cards. Each pack has 7 cards inside. He wants to put these cards in special pages to protect the cards. Each page can hold 10 cards. How many pages does he need to buy?"""
    # Determine the total number of cards
    total_cards = 60 * 7

    # Determine the number of pages needed
    pages_needed = total_cards // 10
    if total_cards % 10 != 0:
        pages_needed += 1

    # Display the number of pages needed
    result = pages_needed
    return result

print(solution())