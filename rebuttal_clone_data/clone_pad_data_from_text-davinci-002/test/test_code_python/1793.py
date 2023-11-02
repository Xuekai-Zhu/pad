def solution():
    ads_page1 = 12
    ads_page2 = 2 * ads_page1
    ads_page3 = ads_page2 + 24
    ads_page4 = (3/4) * ads_page2
    total_ads = ads_page1 + ads_page2 + ads_page3 + ads_page4
    ads_clicked = (2/3) * total_ads
    result = ads_clicked
    return result

print(solution())