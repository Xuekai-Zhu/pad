def solution():
    """Cristian has 50 more black cookies in his cookie jar than white cookies. He eats half of the black cookies and 3/4 of the white cookies. If he initially had 80 white cookies, how many cookies are remaining within the cookie jar altogether?"""
    white_cookies = 80
    black_cookies = white_cookies + 50
    black_cookies_eaten = black_cookies / 2
    white_cookies_eaten = (3/4) * white_cookies
    remaining_cookies = white_cookies + black_cookies - black_cookies_eaten - white_cookies_eaten
    result = remaining_cookies
    return result

print(solution())