def solution():
    # Calculate the number of cookies baked by Jake and Tory
    jake_cookies = 2 * 72
    tory_cookies = 0.5 * (72 + jake_cookies)

    # Calculate the total number of cookies
    total_cookies = 72 + jake_cookies + tory_cookies

    # Calculate the total earnings from selling the cookies
    total_earnings = total_cookies * 2
    result = total_earnings
    return result

print(solution())