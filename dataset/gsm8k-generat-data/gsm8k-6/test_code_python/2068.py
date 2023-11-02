def solution():
    # Calculate the total number of baseball cards Janessa has
    total_cards = 4 + 13 + 36 - 4  # Janessa starts with 4 cards, her father gives her 13, she orders 36 from eBay, but throws away 4 bad cards

    # Calculate the number of cards Janessa kept for herself
    cards_kept = total_cards - 29  # Janessa gave 29 cards to Dexter
    result = cards_kept
    return result

print(solution())