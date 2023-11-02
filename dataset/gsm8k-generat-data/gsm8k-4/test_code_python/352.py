def solution():
    """Punger collects baseball cards. He buys 60 packs of baseball cards. Each pack has 7 cards inside. He wants to put these cards in special pages to protect the cards. Each page can hold 10 cards. How many pages does he need to buy?"""
    # Calculate the total number of cards
    total_cards = 60 * 7

    # Calculate the number of pages needed
    pages_needed = total_cards // 10

    # If there are any leftover cards, add an additional page
    if total_cards % 10 != 0:
        pages_needed += 1

    # return the result
    result = pages_needed
    return result

print(solution())