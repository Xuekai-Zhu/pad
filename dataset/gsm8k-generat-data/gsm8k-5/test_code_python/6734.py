def solution():
    total_cookies = 120  # Katrina has 120 cookies to sell
    cookies_sold_morning = 3 * 12  # 3 dozen cookies sold in the morning
    cookies_sold_lunch = 57  # 57 cookies sold during lunch rush
    cookies_sold_afternoon = 16  # 16 more cookies sold in the afternoon

    # Calculate the total cookies sold
    cookies_sold_total = cookies_sold_morning + cookies_sold_lunch + cookies_sold_afternoon

    # Calculate the cookies left to take home
    cookies_left = total_cookies - cookies_sold_total
    result = cookies_left
    return result

print(solution())