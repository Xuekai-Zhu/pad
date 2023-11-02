def solution():
    
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