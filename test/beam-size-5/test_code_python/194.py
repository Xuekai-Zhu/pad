def solution():
    
    initial_cards = 20
    first_month_cards = initial_cards * 3
    second_month_cards = first_month_cards - 20
    third_month_cards = 2 * (first_month_cards + second_month_cards)
    total_cards = initial_cards + first_month_cards + second_month_cards + third_month_cards
    result = total_cards
    return result

print(solution())