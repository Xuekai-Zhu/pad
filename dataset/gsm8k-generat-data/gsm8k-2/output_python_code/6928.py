def solution():
    """Matt has 8 baseball cards worth $6 each. If he trades two of them to Jane in exchange for 3 $2 cards and 1 $9 card, how much profit does he make?"""
    original_value = 8 * 6
    traded_value = 2 * 6
    received_value = 3 * 2 + 9
    profit = received_value - traded_value
    result = profit
    return result

print(solution())