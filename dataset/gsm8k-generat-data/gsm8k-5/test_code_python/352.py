def solution():
    packs_of_baseball_cards = 60  # Punger has bought 60 packs of baseball cards
    cards_per_pack = 7  # Each pack contains 7 baseball cards
    cards_total = packs_of_baseball_cards * cards_per_pack  # Punger has a total of 420 baseball cards

    cards_per_page = 10  # Each protective page can hold 10 cards
    pages_required = cards_total // cards_per_page  # Calculate how many full protective pages are needed
    if cards_total % cards_per_page != 0:  # If there are any remaining cards
        pages_required += 1  # Add an additional protective page

    result = pages_required
    return result

print(solution())