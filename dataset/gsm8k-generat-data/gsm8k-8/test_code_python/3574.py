def solution():
    # Calculate the number of cookies with nuts
    nuts_cookies = 0.25 * 60

    # Calculate the number of cookies with chocolate chips
    chips_cookies = 0.4 * 60

    # Calculate the number of cookies with both nuts and chocolate chips
    both_cookies = 60 - nuts_cookies - chips_cookies

    # Calculate the total number of nuts needed
    nuts_needed = (nuts_cookies + both_cookies) * 2

    result = nuts_needed
    return result

print(solution())