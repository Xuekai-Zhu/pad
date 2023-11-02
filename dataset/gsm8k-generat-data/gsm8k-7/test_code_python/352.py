def solution():
    num_packs = 60
    cards_per_pack = 7
    cards_per_page = 10

    # Calculate the total number of cards Punger has
    total_cards = num_packs * cards_per_pack

    # Calculate the total number of pages Punger needs
    total_pages = total_cards // cards_per_page

    # If there are any remaining cards, he will need an extra page
    if total_cards % cards_per_page != 0:
        total_pages += 1

    result = total_pages
    return result

print(solution())