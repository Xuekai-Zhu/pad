def solution():
    # Padma starts with 75 cards and trades 2 valuable ones for 10 of Robert's cards
    padma_start = 75
    padma_trade1 = 2
    robert_trade1 = 10

    # Robert starts with 88 cards and trades 8 of his own for 15 of Padma's
    robert_start = 88
    robert_trade2 = 8
    padma_trade2 = 15

    # Total number of cards traded between Padma and Robert
    total_traded = padma_trade1 + robert_trade1 + robert_trade2 + padma_trade2

    result = total_traded
    return result

print(solution())