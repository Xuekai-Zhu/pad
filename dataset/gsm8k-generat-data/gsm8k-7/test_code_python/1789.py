def solution():
    padma_start = 75
    robert_start = 88

    # Padma trades 2 cards for 10 of Robert's cards
    padma_trade_1 = 2
    robert_trade_1 = 10

    # Robert trades 8 of his cards for 15 of Padma's cards
    padma_trade_2 = 15
    robert_trade_2 = 8

    # Calculate the ending number of cards for Padma and Robert
    padma_end = padma_start - padma_trade_1 + padma_trade_2
    robert_end = robert_start - robert_trade_1 + robert_trade_2

    # Calculate the total number of cards traded
    cards_traded = (padma_trade_1 + robert_trade_1) + (padma_trade_2 + robert_trade_2)
    result = cards_traded
    return result

print(solution())