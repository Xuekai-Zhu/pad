def solution():
    """Meena bakes 5 dozen cookies for the school’s bake sale. She sells 2 dozen cookies to her biology teacher, Mr. Stone. Her friend Brock buys 7 cookies, and her friend Katy buys twice as many as Brock. How many cookies does Meena have left?"""
    # Define the initial amount of cookies
    INITIAL_COOKIES = 5 * 12

    # Calculate the amount of cookies sold to Mr. Stone
    mr_stone_cookies = 2 * 12

    # Calculate the amount of cookies sold to Brock
    brock_cookies = 7

    # Calculate the amount of cookies sold to Katy
    katy_cookies = 2 * brock_cookies

    # Calculate the total amount of cookies sold
    total_cookies_sold = mr_stone_cookies + brock_cookies + katy_cookies

    # Calculate the amount of cookies left
    cookies_left = INITIAL_COOKIES - total_cookies_sold

    result = cookies_left
    return result

print(solution())