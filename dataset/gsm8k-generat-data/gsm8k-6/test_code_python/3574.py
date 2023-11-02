def solution():
    # Calculate the number of cookies with nuts only
    nuts_only_cookies = round((1/4) * 60)  # 1/4 of the cookies have nuts in them

    # Calculate the number of cookies with chocolate chips only
    choc_chips_only_cookies = round((40/100) * 60)  # 40% of the cookies have chocolate chips in them

    # Calculate the number of cookies with nuts and chocolate chips
    nuts_choc_chips_cookies = 60 - nuts_only_cookies - choc_chips_only_cookies

    # Calculate the total number of nuts used
    total_nuts_used = (2 * nuts_only_cookies) + (2 * nuts_choc_chips_cookies)

    result = total_nuts_used
    return result

print(solution())