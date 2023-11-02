def solution():
     initial_white_cookies = 80
     black_cookie_increase = 50
     total_black_cookies = initial_white_cookies + black_cookie_increase
     initial_total_cookies = total_black_cookies + initial_white_cookies
     eaten_black_cookies = total_black_cookies / 2
     eaten_white_cookies = initial_white_cookies - (initial_white_cookies / 4)
     total_eaten_cookies = eaten_black_cookies + eaten_white_cookies
     remaining_cookies = initial_total_cookies - total_eaten_cookies
     result = remaining_cookies
     return result

print(solution())