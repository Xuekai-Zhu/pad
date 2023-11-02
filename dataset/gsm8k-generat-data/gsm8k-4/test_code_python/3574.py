def solution():
    """Maria is baking cookies for Sally. Sally says that she wants 1/4 of her cookies to have nuts in them, 40% to have chocolate chips in them, and the remainder to have nuts and chocolate chips in them.
    When she adds nuts to the cookies, she uses 2 nuts per cookie. If she makes 60 cookies, how many nuts does she need?"""
    # Define the total number of cookies and the numbers of cookies with nuts and chocolate chips
    total_cookies = 60
    nut_cookies = total_cookies // 4
    chocolate_cookies = total_cookies * 40 // 100

    # Calculate the number of cookies with both nuts and chocolate chips
    nut_and_chocolate_cookies = total_cookies - nut_cookies - chocolate_cookies

    # Calculate the total number of nuts needed
    nuts_needed = nut_cookies * 2 + nut_and_chocolate_cookies * 2

    result = nuts_needed
    return result

print(solution())