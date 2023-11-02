def solution():
    """Cristian has 50 more black cookies in his cookie jar than white cookies. He eats half of the black cookies and 3/4 of the white cookies. If he initially had 80 white cookies, how many cookies are remaining within the cookie jar altogether?"""
    # Define the initial number of white cookies
    white_cookies = 80

    # Calculate the number of black cookies
    black_cookies = white_cookies + 50

    # Calculate the number of black cookies Cristian eats
    eaten_black_cookies = black_cookies / 2

    # Calculate the number of white cookies Cristian eats
    eaten_white_cookies = white_cookies * 0.75

    # Calculate the total number of cookies remaining
    remaining_cookies = white_cookies + black_cookies - eaten_white_cookies - eaten_black_cookies

    # return the result
    result = remaining_cookies
    return result

print(solution())