def solution():
    """Matt has 8 baseball cards worth $6 each. If he trades two of them to Jane in exchange for 3 $2 cards and 1 $9 card, how much profit does he make?"""
    initial_value = 8 * 6
    traded_cards = 2
    cards_received = 3 + 1
    value_received = (3 * 2) + 9
    net_value = value_received - traded_cards * 6
    profit = net_value - initial_value
    result = profit
    return result

print(solution())