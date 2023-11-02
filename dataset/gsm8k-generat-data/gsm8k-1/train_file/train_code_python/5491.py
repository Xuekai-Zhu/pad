def solution():
    """John buys 2 dozen cookies. He eats 3. How many cookies does he have left?"""
    cookies_per_dozen = 12
    cookies_bought = 2 * cookies_per_dozen
    cookies_eaten = 3
    cookies_left = cookies_bought - cookies_eaten
    result = cookies_left
    return result

print(solution())