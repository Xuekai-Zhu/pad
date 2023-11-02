def solution():
    # Cookies baked on Monday
    cookies_monday = 32

    # Cookies baked on Tuesday
    cookies_tuesday = cookies_monday // 2

    # Cookies baked on Wednesday
    cookies_wednesday = 3 * cookies_tuesday - 4

    # Total number of cookies baked
    total_cookies = cookies_monday + cookies_tuesday + cookies_wednesday
    result = total_cookies
    return result

print(solution())