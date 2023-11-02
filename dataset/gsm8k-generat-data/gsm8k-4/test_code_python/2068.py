def solution():
    """Janessa has a plan to give her brother Dexter his first collection of baseball cards. She currently has 4 cards in addition to the 13 that her father gave her. She ordered a collection of 36 cards from eBay. After inspecting the cards she found 4 cards are in bad shape and decides to throw them away. Janessa ended up giving Dexter 29 cards. How many cards did Janessa keep for herself?"""
    # Calculate the total number of cards Janessa had before ordering from eBay
    total_cards_before = 4 + 13

    # Calculate the number of cards Janessa received from eBay
    cards_from_ebay = 36

    # Calculate the total number of cards Janessa had after receiving the cards from eBay
    total_cards_after = total_cards_before + cards_from_ebay

    # Calculate the number of bad cards Janessa threw away
    bad_cards = 4

    # Calculate the number of cards Janessa gave to Dexter
    cards_given_to_dexter = 29

    # Calculate the number of cards Janessa kept for herself
    cards_kept = total_cards_after - cards_given_to_dexter - bad_cards - total_cards_before

    # Return the result
    result = cards_kept
    return result

print(solution())