def solution():
    # Calculate the number of cookies Sabrina's mother gave her
    mother_cookies = 10 / 2

    # Calculate the number of cookies Sabrina gave to her sister
    sister_cookies = (2/3) * (10 + mother_cookies)

    # Calculate the number of cookies Sabrina has left
    remaining_cookies = 20 - 10 - mother_cookies - sister_cookies
    result = remaining_cookies
    return result

print(solution())