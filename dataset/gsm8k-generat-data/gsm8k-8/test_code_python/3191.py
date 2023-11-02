def solution():
    # Calculate the number of ads on the first and second web pages
    ads_on_first_page = 12
    ads_on_second_page = 2 * ads_on_first_page

    # Calculate the number of ads on the third web page
    ads_on_third_page = ads_on_second_page + 24

    # Calculate the number of ads on the fourth web page
    ads_on_fourth_page = (3/4) * ads_on_second_page

    # Calculate the total number of ads Vermont clicked on
    total_ads = ads_on_first_page + ads_on_second_page + ads_on_third_page + ads_on_fourth_page
    clicked_ads = (2/3) * total_ads
    result = clicked_ads
    return result

print(solution())