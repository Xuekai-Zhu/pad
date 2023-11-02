def solution():
    
    page1_ads = 12
    page2_ads = page1_ads * 2
    page3_ads = page2_ads + 24
    page4_ads = page2_ads * 3/4
    total_ads = page1_ads + page2_ads + page3_ads + page4_ads
    clicked_ads = total_ads * 2/3
    result = clicked_ads
    return result

print(solution())