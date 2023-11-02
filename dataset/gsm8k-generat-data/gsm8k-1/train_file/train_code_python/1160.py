def solution():
    """Meena bakes 5 dozen cookies for the school’s bake sale. She sells 2 dozen cookies to her biology teacher, Mr. Stone. Her friend Brock buys 7 cookies, and her friend Katy buys twice as many as Brock. How many cookies does Meena have left?"""
    total_cookies = 5 * 12
    cookies_sold = 2 * 12 + 7 + 2 * 7
    cookies_left = total_cookies - cookies_sold
    result = cookies_left
    return result

print(solution())