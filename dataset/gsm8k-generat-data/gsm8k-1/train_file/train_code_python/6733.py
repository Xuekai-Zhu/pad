def solution():
    """Katrina has 120 cookies to sell at her bakery. She plans to take home any cookies she doesn’t sell by the end of the day. In the morning, she sells 3 dozen cookies. During the lunch rush, she sells 57 cookies. In the afternoon, she sells 16 more cookies. How many cookies does she have left to take home?"""
    total_cookies = 120
    morning_cookies_sold = 3 * 12
    lunch_cookies_sold = 57
    afternoon_cookies_sold = 16
    cookies_sold = morning_cookies_sold + lunch_cookies_sold + afternoon_cookies_sold
    cookies_left = total_cookies - cookies_sold
    result = cookies_left
    return result

print(solution())