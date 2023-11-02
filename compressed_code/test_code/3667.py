def solution():
    
    white_cookies = 80
    black_cookies = white_cookies + 50
    black_cookies_eaten = black_cookies / 2
    white_cookies_eaten = (3/4) * white_cookies
    remaining_cookies = white_cookies + black_cookies - black_cookies_eaten - white_cookies_eaten
    result = remaining_cookies
    return result

print(solution())