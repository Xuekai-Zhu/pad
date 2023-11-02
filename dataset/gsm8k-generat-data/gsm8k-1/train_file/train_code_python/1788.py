def solution():
    """Padma is trading cards with Robert. Padma started with 75 cards and traded 2 or her valuable ones for 10 of Robert's cards. Robert started with 88 of his own cards and traded another 8 of his cards for 15 of Padma's cards. How many cards were traded between both Padma and Robert?"""
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