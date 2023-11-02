def solution():
    num_best_buy_cards = 6
    best_buy_value = 500
    num_walmart_cards = 9
    walmart_value = 200
    codes_sent = 1 * best_buy_value + 2 * walmart_value

    # Calculate the total value of all gift cards
    total_value = num_best_buy_cards * best_buy_value + num_walmart_cards * walmart_value

    # Calculate the value of remaining gift cards
    remaining_value = total_value - codes_sent
    result = remaining_value
    return result

print(solution())