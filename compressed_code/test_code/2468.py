def solution():
    
    cards_per_week = 20
    weeks_per_year = 52
    total_cards = cards_per_week * weeks_per_year
    lost_cards = total_cards / 2
    remaining_cards = total_cards - lost_cards
    result = remaining_cards
    return result

print(solution())