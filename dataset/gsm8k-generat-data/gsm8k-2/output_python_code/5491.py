def solution():
    """John buys 2 dozen cookies. He eats 3. How many cookies does he have left?"""
    cookies_per_dozen = 12
    total_cookies = 2 * cookies_per_dozen
    eaten_cookies = 3
    remaining_cookies = total_cookies - eaten_cookies
    result = remaining_cookies
    return result

print(solution())