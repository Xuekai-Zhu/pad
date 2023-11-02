def solution():
    """Cristian has 50 more black cookies in his cookie jar than white cookies. He eats half of the black cookies and 3/4 of the white cookies. If he initially had 80 white cookies, how many cookies are remaining within the cookie jar altogether?"""
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