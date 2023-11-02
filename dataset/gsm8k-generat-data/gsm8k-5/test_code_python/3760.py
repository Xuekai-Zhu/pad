def solution():
    clementine_cookies = 72
    jake_cookies = 2 * clementine_cookies
    tory_cookies = (clementine_cookies + jake_cookies) / 2
    total_cookies = clementine_cookies + jake_cookies + tory_cookies

    # Calculate the total money made
    total_money = total_cookies * 2
    result = total_money
    return result

print(solution())