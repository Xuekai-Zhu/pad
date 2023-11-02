def solution():
    # Define the number of packs and cards per pack
    num_packs = 60
    cards_per_pack = 7

    # Calculate the total number of cards
    total_cards = num_packs * cards_per_pack

    # Calculate the number of pages needed
    num_pages = total_cards // 10

    # If there are any remaining cards, add an additional page
    if total_cards % 10 != 0:
        num_pages += 1

    result = num_pages
    return result

print(solution())