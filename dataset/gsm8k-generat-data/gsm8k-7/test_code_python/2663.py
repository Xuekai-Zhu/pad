def solution():
    num_cards_given = 2
    card_value_given = 8

    num_cards_received = 1
    card_value_received = 21

    # Calculate the total value of cards given
    total_given_value = num_cards_given * card_value_given

    # Calculate the total value of cards received
    total_received_value = num_cards_received * card_value_received

    # Calculate the profit
    profit = total_received_value - total_given_value
    result = profit
    return result

print(solution())