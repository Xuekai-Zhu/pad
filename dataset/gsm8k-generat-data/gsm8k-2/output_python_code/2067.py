def solution():
    """Janessa has a plan to give her brother Dexter his first collection of baseball cards. She currently has 4 cards in addition to the 13 that her father gave her. She ordered a collection of 36 cards from eBay. After inspecting the cards she found 4 cards are in bad shape and decides to throw them away. Janessa ended up giving Dexter 29 cards. How many cards did Janessa keep for herself?"""
    initial_cards = 4 + 13 + 36
    bad_cards = 4
    remaining_cards = initial_cards - bad_cards - 29
    result = remaining_cards
    return result

print(solution())