def solution():
    """Three companies, A, B, and C, each purchased 10 ad spaces on a newspaper, with each ad space having a size of 12 foot by 5-foot rectangle. If each square foot ad was charged at $60, how much money did the three pay for the ads combined?"""
    ads_per_company = 10
    width = 12
    height = 5
    ad_size = width * height
    price_per_square_foot = 60
    total_ads = ads_per_company * 3
    total_ad_size = ad_size * total_ads
    total_cost = total_ad_size * price_per_square_foot
    result = total_cost
    return result

print(solution())