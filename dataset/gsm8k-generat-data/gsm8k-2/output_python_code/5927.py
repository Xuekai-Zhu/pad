def solution():
    """Three companies, A, B, and C, each purchased 10 ad spaces on a newspaper, with each ad space having a size of 12 foot by 5-foot rectangle. If each square foot ad was charged at $60, how much money did the three pay for the ads combined?"""
    ad_spaces = 10
    ad_size = 12 * 5
    square_foot_price = 60
    total_ads_size = ad_spaces * ad_size * 3
    total_price = total_ads_size * square_foot_price
    result = total_price
    return result

print(solution())