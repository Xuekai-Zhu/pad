def solution():
    num_cards = 8
    card_value = 6
    trade_cards = 2
    trade_card_value = 2
    new_card_value = 9

    # Calculate the total value of Matt's baseball cards
    total_card_value = num_cards * card_value

    # Calculate the value of the cards he traded
    traded_cards_value = trade_cards * card_value

    # Calculate the value of the cards he received in the trade
    trade_value = (3 * trade_card_value) + new_card_value

    # Calculate the total profit
    profit = trade_value - traded_cards_value
    result = profit
    return result

print(solution())