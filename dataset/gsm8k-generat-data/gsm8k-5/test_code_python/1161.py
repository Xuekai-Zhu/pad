def solution():
    cookies_baked = 5 * 12  # Meena bakes 5 dozen cookies, which is 60 cookies
    cookies_sold_teacher = 2 * 12  # Meena sells 2 dozen cookies to the biology teacher, which is 24 cookies
    cookies_sold_Brock = 7  # Brock buys 7 cookies
    cookies_sold_Katy = 2 * cookies_sold_Brock  # Katy buys twice as many as Brock, which is 14 cookies

    # Calculate the total number of cookies sold
    total_cookies_sold = cookies_sold_teacher + cookies_sold_Brock + cookies_sold_Katy

    # Calculate the number of cookies left
    cookies_left = cookies_baked - total_cookies_sold
    result = cookies_left
    return result

print(solution())