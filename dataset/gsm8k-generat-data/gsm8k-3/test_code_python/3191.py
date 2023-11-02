def solution():
    """Vermont opened up 4 web pages on his web browser and found 12 ads on the first web page and twice as many ads on the second web page as the first web page. When he opened the third web page, he found 24 more ads than the number of ads on the second web page. If the fourth web page had 3/4 times as many ads as the second web page, calculate the total number of ads Vermont clicked on if he clicked on 2/3 of them."""
    # Calculate the number of ads on the second web page
    second_page_ads = 12 * 2

    # Calculate the number of ads on the third web page
    third_page_ads = second_page_ads + 24

    # Calculate the number of ads on the fourth web page
    fourth_page_ads = second_page_ads * (3/4)

    # Calculate the total number of ads Vermont found
    total_ads = 12 + second_page_ads + third_page_ads + fourth_page_ads

    # Calculate the number of ads Vermont clicked on
    clicked_ads = total_ads * (2/3)

    # Display the number of ads Vermont clicked on
    result = clicked_ads
    return result

print(solution())