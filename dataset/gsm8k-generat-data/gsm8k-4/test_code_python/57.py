def solution():
    """Liza bought 10 kilograms of butter to make cookies. She used one-half of it for chocolate chip cookies, one-fifth of it for peanut butter cookies, and one-third of the remaining butter for sugar cookies. How many kilograms of butter are left after making those three kinds of cookies?"""
    # Define the initial amount of butter
    butter = 10

    # Calculate the amount of butter used for chocolate chip cookies
    cc_cookies = butter * 0.5
    remaining_butter = butter - cc_cookies

    # Calculate the amount of butter used for peanut butter cookies
    pb_cookies = remaining_butter * 0.2
    remaining_butter -= pb_cookies

    # Calculate the amount of butter used for sugar cookies
    sugar_cookies = remaining_butter * (1/3)
    remaining_butter -= sugar_cookies

    result = remaining_butter
    return result

print(solution())