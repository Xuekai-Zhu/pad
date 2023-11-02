def solution():
    cookies_on_monday = 32
    cookies_on_tuesday = cookies_on_monday / 2
    cookies_on_wednesday = 3 * cookies_on_tuesday
    cookies_eaten_on_wednesday = 4
    total_cookies = cookies_on_monday + cookies_on_tuesday + cookies_on_wednesday - cookies_eaten_on_wednesday
    result = total_cookies
    return result

print(solution())