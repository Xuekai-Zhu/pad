def solution():
    """Punger collects baseball cards. He buys 60 packs of baseball cards. Each pack has 7 cards inside. He wants to put these cards in special pages to protect the cards. Each page can hold 10 cards. How many pages does he need to buy?"""
    packs_of_cards = 60
    cards_per_pack = 7
    cards_total = packs_of_cards * cards_per_pack
    cards_per_page = 10
    pages_needed = cards_total // cards_per_page + (cards_total % cards_per_page > 0)
    result = pages_needed
    return result

print(solution())