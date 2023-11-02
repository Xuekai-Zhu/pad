def solution():
    """Out of the 200 cookies that Javier baked from the recipe he learned online, his wife took 30%, and his daughter took 40 from the remaining cookies. If he ate half of the remaining cookies, how many cookies did they not eat?"""
    # Define the initial number of cookies
    initial_cookies = 200

    # Calculate the number of cookies his wife took
    wife_cookies = initial_cookies * 0.3

    # Calculate the number of cookies remaining after his wife took some
    remaining_cookies = initial_cookies - wife_cookies

    # Calculate the number of cookies his daughter took
    daughter_cookies = 40

    # Calculate the number of cookies remaining after his daughter took some
    remaining_cookies -= daughter_cookies

    # Calculate the number of cookies he ate
    he_cookies = remaining_cookies / 2

    # Calculate the number of cookies they did not eat
    not_eaten_cookies = remaining_cookies - he_cookies

    # return the result
    result = not_eaten_cookies
    return result

print(solution())