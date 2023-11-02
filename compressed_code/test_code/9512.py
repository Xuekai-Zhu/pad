def solution():
    
    white_cookies = 80
    black_cookies = white_cookies + 50
    eaten_black_cookies = black_cookies / 2
    eaten_white_cookies = white_cookies * 3/4
    remaining_black_cookies = black_cookies - eaten_black_cookies
    remaining_white_cookies = white_cookies - eaten_white_cookies
    total_remaining_cookies = remaining_black_cookies + remaining_white_cookies
    result = total_remaining_cookies
    return result

print(solution())