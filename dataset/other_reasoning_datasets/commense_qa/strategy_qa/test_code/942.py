def solution():
    china_trade_share = 12.4
    eic_trade_share = 50.0
    if china_trade_share < eic_trade_share:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())