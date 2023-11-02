def solution():
    """Katrina has 120 cookies to sell at her bakery. She plans to take home any cookies she doesn’t sell by the end of the day. In the morning, she sells 3 dozen cookies. During the lunch rush, she sells 57 cookies. In the afternoon, she sells 16 more cookies. How many cookies does she have left to take home?"""
    cookies_sold_morning = 3 * 12
    cookies_sold_lunch = 57
    cookies_sold_afternoon = 16
    total_cookies_sold = cookies_sold_morning + cookies_sold_lunch + cookies_sold_afternoon
    cookies_left = 120 - total_cookies_sold
    result = cookies_left
    return result

print(solution())