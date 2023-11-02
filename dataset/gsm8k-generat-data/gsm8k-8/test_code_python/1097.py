def solution():
    # Calculate the number of cookies Javier's wife took
    wife_cookies = 0.3 * 200

    # Calculate the number of cookies Javier had left after his wife took some
    remaining_cookies = 200 - wife_cookies

    # Calculate the number of cookies Javier's daughter took
    daughter_cookies = 40

    # Calculate the number of cookies Javier had left after his daughter took some
    remaining_cookies -= daughter_cookies

    # Calculate the number of cookies Javier ate
    eaten_cookies = remaining_cookies / 2

    # Calculate the number of cookies not eaten
    not_eaten_cookies = remaining_cookies - eaten_cookies

    result = not_eaten_cookies
    return result

print(solution())