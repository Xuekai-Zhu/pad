def solution():
     cookies_ eaten_Monday = 5
     cookies_ eaten_Tuesday = cookies_eaten_Monday * 2
     cookies_eaten_Wednesday = cookies_eaten_Tuesday + (cookies_eaten_Tuesday * 0.4)
     total_cookies = cookies_eaten_Monday + cookies_eaten_Tuesday + cookies_eaten_Wednesday
     result = total_cookies
     return result

print(solution())