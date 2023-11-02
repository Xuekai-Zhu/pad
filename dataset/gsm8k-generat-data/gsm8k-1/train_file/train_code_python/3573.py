def solution():
    """Maria is baking cookies for Sally. Sally says that she wants 1/4 of her cookies to have nuts in them, 40% to have chocolate chips in them, and the remainder to have nuts and chocolate chips in them. 
    When she adds nuts to the cookies, she uses 2 nuts per cookie. If she makes 60 cookies, how many nuts does she need?"""
    total_cookies = 60
    nuts_cookies = total_cookies * (1/4)
    choco_cookies = total_cookies * (40/100)
    nuts_choco_cookies = total_cookies - nuts_cookies - choco_cookies
    nuts_needed = nuts_cookies * 2
    result = nuts_needed
    return result

print(solution())