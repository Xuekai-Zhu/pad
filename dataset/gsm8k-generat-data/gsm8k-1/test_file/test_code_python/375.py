def solution():
    """Rachel bought 23 cookies and Janet gave her 42 cookies. The other day her brother ate 44 of those cookies. How many cookies are left for Rachel?"""
    total_cookies = 23 + 42
    cookies_eaten = 44
    cookies_left = total_cookies - cookies_eaten
    result = cookies_left
    return result

print(solution())