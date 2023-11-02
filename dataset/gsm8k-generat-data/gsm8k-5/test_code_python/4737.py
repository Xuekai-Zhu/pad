def solution():
    white_cookies = 80  # Cristian initially had 80 white cookies
    black_cookies = white_cookies + 50  # Cristian had 50 more black cookies than white cookies

    # Calculate how many cookies are left after Cristian eats them
    black_cookies_left = black_cookies / 2  # Cristian eats half of the black cookies
    white_cookies_left = white_cookies / 4  # Cristian eats 3/4 of the white cookies

    total_cookies_left = black_cookies_left + white_cookies_left
    result = total_cookies_left
    return result

print(solution())