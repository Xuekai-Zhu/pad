def solution():
    packs_of_cards = 60
    cards_per_pack = 7
    cards_per_page = 10
    total_cards = packs_of_cards * cards_per_pack
    total_pages = total_cards // cards_per_page
    result = total_pages
    return result

print(solution())