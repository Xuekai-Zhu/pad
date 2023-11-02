def solution():
    cookies_baked = 20  # Neil baked 20 cookies
    cookies_given = (2/5) * cookies_baked  # Neil gave away 2/5 of the cookies
    cookies_left = cookies_baked - cookies_given  # Neil has the remaining cookies

    result = cookies_left
    return result

print(solution())