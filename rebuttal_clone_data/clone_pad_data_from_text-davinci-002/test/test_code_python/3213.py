def solution():
    suit_price = 700.00
    shirt_price = 50.00
    loafer_price = 150.00
    commission_rate = 15
    commission_suit = suit_price * (commission_rate / 100)
    commission_shirt = shirt_price * (commission_rate / 100)
    commission_loafer = loafer_price * (commission_rate / 100)
    total_commission = (commission_suit * 2) + (commission_shirt * 6) + (commission_loafer * 2)
    result = total_commission
    return result

print(solution())