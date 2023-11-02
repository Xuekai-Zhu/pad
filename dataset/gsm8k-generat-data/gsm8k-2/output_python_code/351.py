def solution():
    """Punger collects baseball cards. He buys 60 packs of baseball cards. Each pack has 7 cards inside. He wants to put these cards in special pages to protect the cards. Each page can hold 10 cards. How many pages does he need to buy?"""
    total_cards = 60 * 7
    cards_per_page = 10
    pages_needed = total_cards // cards_per_page + (total_cards % cards_per_page > 0)
    result = pages_needed
    return result

print(solution())