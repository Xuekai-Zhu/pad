def solution():
    num_cookies = 19

    # Calculate the number of cookies left after giving 5 to a friend
    num_cookies_left = num_cookies - 5

    # Calculate the number of cookies to give to family
    num_family_cookies = num_cookies_left / 2

    # Calculate the number of cookies left after eating 2
    num_cookies_left -= 2

    # Calculate the final number of cookies
    result = num_cookies_left
    return result

print(solution())