def solution():
    
    initial_cards = 20
    cards_collected_first_month = initial_cards * 3
    cards_collected_second_month = cards_collected_first_month - 20
    cards_collected_third_month = (cards_collected_first_month + cards_collected_second_month) * 2
    total_cards = initial_cards + cards_collected_first_month + cards_collected_second_month + cards_collected_third_month
    result = total_cards
    return result

print(solution())