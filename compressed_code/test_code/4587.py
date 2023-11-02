def solution():
    
    ad_spaces = 10
    ad_size = 12 * 5
    square_foot_price = 60
    total_ads_size = ad_spaces * ad_size * 3
    total_price = total_ads_size * square_foot_price
    result = total_price
    return result

print(solution())