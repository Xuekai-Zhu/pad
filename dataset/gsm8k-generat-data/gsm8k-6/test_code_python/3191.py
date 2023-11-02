def solution():
    # Calculate the number of ads on the second web page
    second_webpage_ads = 12 * 2  # Twice as many ads as the first web page
    
    # Calculate the number of ads on the third web page
    third_webpage_ads = second_webpage_ads + 24  # 24 more ads than the number of ads on the second web page
    
    # Calculate the number of ads on the fourth web page
    fourth_webpage_ads = (3/4) * second_webpage_ads  # 3/4 times as many ads as the second web page
    
    # Calculate the total number of ads Vermont clicked on
    total_ads = 12 + second_webpage_ads + third_webpage_ads + fourth_webpage_ads  # Total number of ads on all four web pages
    clicked_ads = (2/3) * total_ads  # Vermont clicked on 2/3 of the total ads
    
    result = clicked_ads
    return result

print(solution())