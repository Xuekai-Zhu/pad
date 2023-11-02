def solution():
    num_packs = 3
    pack_price = 1800
    num_cards_1 = 4000
    card_price = 1000
    num_cards_2 = 30
    average_price = 50

    # Calculate the total cost of all packs
    total_cost = num_packs * pack_price

    # Calculate the total value of the cards
    total_card_value = (num_cards_1 * card_price) + (num_cards_2 * card_price)

    # Calculate the total value of the cards
    total_card_value = (num_cards_1 * card_price) + (num_cards_2 * average_price)

    # Calculate the total profit
    total_profit = total_card_value - total_cost
    result = total_profit
    return result

print(solution())