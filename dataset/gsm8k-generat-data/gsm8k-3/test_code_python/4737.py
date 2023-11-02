def solution():
    """Cristian has 50 more black cookies in his cookie jar than white cookies. He eats half of the black cookies and 3/4 of the white cookies. If he initially had 80 white cookies, how many cookies are remaining within the cookie jar altogether?"""
    # Define the initial number of white cookies
    white_cookies = 80

    # Calculate the number of black cookies
    black_cookies = white_cookies + 50

    # Calculate the number of black cookies remaining after Cristian eats half of them
    black_cookies_remaining = black_cookies / 2

    # Calculate the number of white cookies remaining after Cristian eats 3/4 of them
    white_cookies_remaining = white_cookies / 4

    # Calculate the total number of cookies remaining
    total_cookies_remaining = black_cookies_remaining + white_cookies_remaining

    # Display the total number of cookies remaining
    result = total_cookies_remaining
    return result

print(solution())