def solution():
    """The fisherman gets 8 Red snappers and 14 Tunas every day. If a Red snapper costs $3 and a Tuna costs $2, how much does he earn every day?"""
    red_snapper_count = 8
    tuna_count = 14
    red_snapper_price = 3
    tuna_price = 2
    total_red_snapper_earnings = red_snapper_count * red_snapper_price
    total_tuna_earnings = tuna_count * tuna_price
    daily_earnings = total_red_snapper_earnings + total_tuna_earnings
    result = daily_earnings
    return result

print(solution())