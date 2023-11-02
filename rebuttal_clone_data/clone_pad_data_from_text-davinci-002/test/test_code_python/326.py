def solution():
    total_cards = 1000
    num_kids = 30
    cards_per_kid = 8
    total_cards_needed = total_cards - (num_kids * cards_per_kid)
    result = total_cards_needed
    
    return result

print(solution())