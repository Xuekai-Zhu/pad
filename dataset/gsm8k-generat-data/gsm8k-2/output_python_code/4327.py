def solution():
    """The fisherman gets 8 Red snappers and 14 Tunas every day. If a Red snapper costs $3 and a Tuna costs $2, how much does he earn every day?"""
    red_snapper_count = 8
    tuna_count = 14
    red_snapper_price = 3
    tuna_price = 2
    total_red_snapper_price = red_snapper_count * red_snapper_price
    total_tuna_price = tuna_count * tuna_price
    total_earnings = total_red_snapper_price + total_tuna_price
    result = total_earnings
    return result

print(solution())