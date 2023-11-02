def solution():
    
    padma_start = 75
    robert_start = 88
    padma_to_robert_cards = 2
    padma_to_robert_trade = 10
    robert_to_padma_cards = 8
    robert_to_padma_trade = 15
    total_cards_traded = (padma_to_robert_cards + robert_to_padma_cards) + (padma_to_robert_trade + robert_to_padma_trade)
    result = total_cards_traded
    return result

print(solution())