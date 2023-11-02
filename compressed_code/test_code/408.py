def solution():
    
    best_buy_cards = 6
    best_buy_value = 500
    walmart_cards = 9
    walmart_value = 200
    codes_sent = (1 * best_buy_value) + (2 * walmart_value)
    total_value = (best_buy_cards * best_buy_value) + (walmart_cards * walmart_value)
    remaining_value = total_value - codes_sent
    result = remaining_value
    return result

print(solution())