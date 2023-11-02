def solution():
    total_cookies = 256  # Uncle Jude baked 256 cookies
    cookies_to_tim = 15  # He gave 15 cookies to Tim
    cookies_to_mike = 23  # He gave 23 cookies to Mike
    cookies_to_anna = 2 * cookies_to_tim  # He gave twice as many cookies as he gave to Tim to Anna
    cookies_in_fridge = total_cookies - cookies_to_tim - cookies_to_mike - cookies_to_anna  # He kept some in the fridge

    result = cookies_in_fridge
    return result

print(solution())