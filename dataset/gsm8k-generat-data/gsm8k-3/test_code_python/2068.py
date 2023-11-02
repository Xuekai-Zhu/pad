def solution():
    """Janessa has a plan to give her brother Dexter his first collection of baseball cards. She currently has 4 cards in addition to the 13 that her father gave her.  She ordered a collection of 36 cards from eBay. After inspecting the cards she found 4 cards are in bad shape and decides to throw them away. Janessa ended up giving Dexter 29 cards. How many cards did Janessa keep for herself?"""
    # Define the initial number of cards Janessa has
    initial_cards = 4 + 13

    # Define the number of cards ordered from eBay
    ebay_cards = 36

    # Define the number of bad cards
    bad_cards = 4

    # Define the number of cards given to Dexter
    dexter_cards = 29

    # Calculate the number of cards Janessa kept for herself
    kept_cards = initial_cards + ebay_cards - bad_cards - dexter_cards

    # Display the number of cards Janessa kept for herself
    result = kept_cards
    return result

print(solution())