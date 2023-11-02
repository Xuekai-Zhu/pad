def solution():
    num_ads_1 = 12
    num_ads_2 = num_ads_1 * 2
    num_ads_3 = num_ads_2 + 24
    num_ads_4 = num_ads_2 * 0.75
    total_ads = num_ads_1 + num_ads_2 + num_ads_3 + num_ads_4
    clicked_ads = total_ads * (2/3)
    result = clicked_ads
    return result

print(solution())