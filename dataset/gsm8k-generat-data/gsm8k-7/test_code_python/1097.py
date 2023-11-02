def solution():
    total_cookies = 200
    wife_share = 0.3
    daughter_share = 40

    # Calculate the number of cookies taken by Javier's wife
    wife_cookies = total_cookies * wife_share

    # Calculate the remaining cookies after Javier's wife took her share
    remaining_cookies = total_cookies - wife_cookies

    # Calculate the number of cookies taken by Javier's daughter
    daughter_cookies = daughter_share

    # Calculate the number of cookies left after Javier and his daughter ate half of the remaining cookies
    remaining_cookies = remaining_cookies - daughter_cookies - (remaining_cookies / 2)

    result = remaining_cookies
    return result

print(solution())