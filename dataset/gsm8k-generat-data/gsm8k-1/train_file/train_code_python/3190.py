def solution():
    """Vermont opened up 4 web pages on his web browser and found 12 ads on the first web page and twice as many ads on the second web page as the first web page. When he opened the third web page, he found 24 more ads than the number of ads on the second web page. If the fourth web page had 3/4 times as many ads as the second web page, calculate the total number of ads Vermont clicked on if he clicked on 2/3 of them."""
    page1_ads = 12
    page2_ads = page1_ads * 2
    page3_ads = page2_ads + 24
    page4_ads = page2_ads * 3/4
    total_ads = page1_ads + page2_ads + page3_ads + page4_ads
    clicked_ads = total_ads * 2/3
    result = clicked_ads
    return result

print(solution())