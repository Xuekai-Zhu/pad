def solution():
    """Maria is baking cookies for Sally. Sally says that she wants 1/4 of her cookies to have nuts in them, 40% to have chocolate chips in them, and the remainder to have nuts and chocolate chips in them. When she adds nuts to the cookies, she uses 2 nuts per cookie. If she makes 60 cookies, how many nuts does she need?"""
    # Define the number of cookies and the percentages of nuts and chocolate chips
    TOTAL_COOKIES = 60
    NUTS_PERCENTAGE = 0.25
    CHOCOLATE_CHIPS_PERCENTAGE = 0.4

    # Calculate the number of cookies with nuts
    nuts_cookies = int(TOTAL_COOKIES * NUTS_PERCENTAGE)

    # Calculate the number of cookies with chocolate chips
    chocolate_chips_cookies = int(TOTAL_COOKIES * CHOCOLATE_CHIPS_PERCENTAGE)

    # Calculate the number of cookies with both nuts and chocolate chips
    nuts_and_chocolate_chips_cookies = TOTAL_COOKIES - nuts_cookies - chocolate_chips_cookies

    # Calculate the total number of nuts needed
    nuts_needed = (nuts_cookies + nuts_and_chocolate_chips_cookies) * 2

    # Display the total number of nuts needed
    result = nuts_needed
    return result

print(solution())