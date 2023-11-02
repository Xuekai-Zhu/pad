def solution():
    # Calculate the total value of Matt's baseball cards
    total_value = 8 * 6

    # Calculate the total value of the cards he trades with Jane
    traded_value = 2 * 6

    # Calculate the total value of the cards he receives from Jane
    received_value = 3 * 2 + 1 * 9

    # Calculate the total profit
    total_profit = received_value - traded_value

    result = total_profit
    return result

print(solution())