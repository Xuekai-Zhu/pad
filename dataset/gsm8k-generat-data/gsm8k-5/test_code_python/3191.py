def solution():
    # Number of ads on the first web page
    ads_first_page = 12 

    # Number of ads on the second web page
    ads_second_page = ads_first_page * 2 

    # Number of ads on the third web page
    ads_third_page = ads_second_page + 24 

    # Number of ads on the fourth web page
    ads_fourth_page = ads_second_page * 3/4 

    # Total number of ads Vermont saw
    total_ads = ads_first_page + ads_second_page + ads_third_page + ads_fourth_page 

    # Number of ads Vermont clicked on
    clicked_ads = total_ads * 2/3 

    result = clicked_ads
    return result

print(solution())