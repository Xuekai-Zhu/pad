def solution():
    total_cookies = 200  # Javier baked 200 cookies
    wife_share = 0.3  # Javier's wife took 30% of the cookies
    daughter_share = 40  # Javier's daughter took 40 cookies

    # Calculate the number of cookies left after Javier's wife took her share
    remaining_cookies = total_cookies - (total_cookies * wife_share)

    # Calculate the number of cookies left after Javier's daughter took her share
    remaining_cookies -= daughter_share

    # Calculate the number of cookies Javier ate
    javier_share = remaining_cookies / 2

    # Calculate the number of cookies left
    cookies_left = remaining_cookies - javier_share
    result = cookies_left
    return result

print(solution())