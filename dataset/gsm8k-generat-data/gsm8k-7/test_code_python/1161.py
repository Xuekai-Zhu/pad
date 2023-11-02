def solution():
    num_cookies = 5 * 12  # 5 dozen cookies

    # Meena sells 2 dozen cookies to Mr. Stone
    num_cookies -= 2 * 12

    # Meena's friend Brock buys 7 cookies
    num_cookies -= 7

    # Meena's friend Katy buys twice as many as Brock
    num_cookies -= 2 * 7

    result = num_cookies
    return result

print(solution())