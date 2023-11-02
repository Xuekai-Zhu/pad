def solution():
    """Nicky is trading baseball cards with Jill. If Nicky trades two cards worth $8 each for 1 card worth $21, how many dollars of profit does he make?"""
    cost_of_cards_traded = 2 * 8
    cost_of_card_received = 21
    profit = cost_of_card_received - cost_of_cards_traded
    result = profit
    return result

print(solution())