def solution():
    # Calculate the total number of cookies baked
    clementine_cookies = 72
    jake_cookies = 2*clementine_cookies
    tory_cookies = (clementine_cookies + jake_cookies) / 2
    total_cookies = clementine_cookies + jake_cookies + tory_cookies

    # Calculate the total amount of money made from selling the cookies
    money_made = total_cookies * 2
    result = money_made
    return result

print(solution())