def solution():
    """Out of the 200 cookies that Javier baked from the recipe he learned online, his wife took 30%, and his daughter took 40 from the remaining cookies. If he ate half of the remaining cookies, how many cookies did they not eat?"""
    # Define the number of cookies Javier baked
    num_cookies = 200

    # Calculate the number of cookies his wife took
    wife_cookies = int(num_cookies * 0.3)

    # Calculate the number of cookies remaining after his wife took hers
    remaining_cookies = num_cookies - wife_cookies

    # Calculate the number of cookies his daughter took
    daughter_cookies = 40

    # Calculate the number of cookies Javier ate
    javier_cookies = int(remaining_cookies / 2)

    # Calculate the number of cookies not eaten
    not_eaten_cookies = remaining_cookies - daughter_cookies - javier_cookies

    # Display the number of cookies not eaten
    result = not_eaten_cookies
    return result

print(solution())