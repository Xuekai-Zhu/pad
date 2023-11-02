def solution():
    """Vermont opened up 4 web pages on his web browser and found 12 ads on the first web page and twice as many ads on the second web page as the first web page. When he opened the third web page, he found 24 more ads than the number of ads on the second web page. If the fourth web page had 3/4 times as many ads as the second web page, calculate the total number of ads Vermont clicked on if he clicked on 2/3 of them."""
    # Calculate the number of ads on the first web page
    ads_on_first_page = 12

    # Calculate the number of ads on the second web page
    ads_on_second_page = ads_on_first_page * 2

    # Calculate the number of ads on the third web page
    ads_on_third_page = ads_on_second_page + 24

    # Calculate the number of ads on the fourth web page
    ads_on_fourth_page = ads_on_second_page * 3 / 4

    # Calculate the total number of ads Vermont saw
    total_ads = ads_on_first_page + ads_on_second_page + ads_on_third_page + ads_on_fourth_page

    # Calculate the number of ads Vermont clicked on
    clicked_ads = total_ads * 2 / 3

    # return the result
    result = int(clicked_ads)
    return result

print(solution())