def solution():
    """John buys 2 dozen cookies. He eats 3. How many cookies does he have left?"""
    COOKIES_PER_DOZEN = 12 # number of cookies in a dozen
    cookies_bought = 2 * COOKIES_PER_DOZEN # total number of cookies bought
    cookies_eaten = 3 # number of cookies eaten
    cookies_left = cookies_bought - cookies_eaten # number of cookies left
    result = cookies_left
    return result

print(solution())