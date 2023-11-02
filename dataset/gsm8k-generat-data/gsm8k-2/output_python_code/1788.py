def solution():
    """Padma is trading cards with Robert. Padma started with 75 cards and traded 2 or her valuable ones for 10 of Robert's cards. Robert started with 88 of his own cards and traded another 8 of his cards for 15 of Padma's cards. How many cards were traded between both Padma and Robert?"""
    padma_start = 75
    robert_start = 88
    padma_trade1 = 2
    robert_trade1 = 10
    robert_trade2 = 8
    padma_trade2 = 15

    padma_end = padma_start - padma_trade1 + robert_trade1 - padma_trade2
    robert_end = robert_start - robert_trade1 + padma_trade1 - robert_trade2

    total_traded = padma_trade1 + robert_trade1 + robert_trade2 + padma_trade2

    result = total_traded
    return result

print(solution())