def solution():
    
    page1_ads = 12
    page2_ads = 2 * page1_ads
    page3_ads = page2_ads + 24
    page4_ads = 3/4 * page2_ads
    
    total_ads = page1_ads + page2_ads + page3_ads + page4_ads
    clicked_on = 2/3 * total_ads
    
    result = clicked_on
    return result

print(solution())