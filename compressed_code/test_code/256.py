def solution():
    
    total_cards = 60 * 7
    cards_per_page = 10
    pages_needed = total_cards // cards_per_page + (total_cards % cards_per_page > 0)
    result = pages_needed
    return result

print(solution())