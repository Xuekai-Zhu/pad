def solution():
    """Maria is baking cookies for Sally. Sally says that she wants 1/4 of her cookies to have nuts in them, 40% to have chocolate chips in them, and the remainder to have nuts and chocolate chips in them. When she adds nuts to the cookies, she uses 2 nuts per cookie. If she makes 60 cookies, how many nuts does she need?"""
    total_cookies = 60
    nut_cookies = int(total_cookies * 0.25)
    choc_cookies = int(total_cookies * 0.4)
    nut_and_choc_cookies = total_cookies - nut_cookies - choc_cookies
    total_nuts = (nut_cookies + nut_and_choc_cookies) * 2
    result = total_nuts
    return result

print(solution())