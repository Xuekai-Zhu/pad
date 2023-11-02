def solution():
    """An 18-month magazine subscription is normally $34. The magazine is currently running a promotion for $0.25 off each twice-a-month issue when signing up for the 18-month subscription. How many dollars cheaper is the promotional subscription than the normal one?"""
    normal_price = 34
    promo_price = normal_price - (0.25 * 36)
    difference = normal_price - promo_price
    result = difference
    return result

print(solution())