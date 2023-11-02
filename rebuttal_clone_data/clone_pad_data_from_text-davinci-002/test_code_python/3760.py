def solution():
     clementine_cookies = 72
     jake_cookies = clementine_cookies * 2
     tory_cookies = (clementine_cookies + jake_cookies) / 2
     total_cookies = clementine_cookies + jake_cookies + tory_cookies
     cookie_price = 2
     total_revenue = total_cookies * cookie_price
     result = total_revenue
     return result

print(solution())