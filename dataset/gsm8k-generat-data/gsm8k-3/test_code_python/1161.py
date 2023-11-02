def solution():
    """Meena bakes 5 dozen cookies for the school’s bake sale.  She sells 2 dozen cookies to her biology teacher, Mr. Stone.  Her friend Brock buys 7 cookies, and her friend Katy buys twice as many as Brock.  How many cookies does Meena have left?"""
    # Define the number of cookies in a dozen
    COOKIES_PER_DOZEN = 12

    # Define the number of dozens Meena bakes
    dozens_baked = 5

    # Calculate the total number of cookies Meena bakes
    total_cookies = dozens_baked * COOKIES_PER_DOZEN

    # Calculate the number of cookies sold to Mr. Stone
    cookies_sold_mr_stone = 2 * COOKIES_PER_DOZEN

    # Calculate the number of cookies sold to Brock
    cookies_sold_brock = 7

    # Calculate the number of cookies sold to Katy
    cookies_sold_katy = 2 * cookies_sold_brock

    # Calculate the total number of cookies sold
    cookies_sold_total = cookies_sold_mr_stone + cookies_sold_brock + cookies_sold_katy

    # Calculate the number of cookies remaining
    cookies_remaining = total_cookies - cookies_sold_total

    # Display the number of cookies remaining
    result = cookies_remaining
    return result

print(solution())