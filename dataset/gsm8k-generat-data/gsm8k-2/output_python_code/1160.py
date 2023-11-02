def solution():
    """Meena bakes 5 dozen cookies for the school’s bake sale. She sells 2 dozen cookies to her biology teacher, Mr. Stone. Her friend Brock buys 7 cookies, and her friend Katy buys twice as many as Brock. How many cookies does Meena have left?"""
    total_cookies = 5 * 12
    mr_stone_cookies = 2 * 12
    brock_cookies = 7
    katy_cookies = 2 * brock_cookies

    total_sold_cookies = mr_stone_cookies + brock_cookies + katy_cookies
    remaining_cookies = total_cookies - total_sold_cookies
    result = remaining_cookies
    return result

print(solution())