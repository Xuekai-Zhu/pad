def solution():
    """Liza bought 10 kilograms of butter to make cookies. She used one-half of it for chocolate chip cookies, one-fifth of it for peanut butter cookies, and one-third of the remaining butter for sugar cookies. How many kilograms of butter are left after making those three kinds of cookies?"""
    # Define the initial amount of butter
    butter = 10.0

    # Calculate the amount of butter used for chocolate chip cookies
    cc_butter = butter * 1/2

    # Calculate the amount of butter used for peanut butter cookies
    pb_butter = butter * 1/5

    # Calculate the remaining amount of butter
    remaining_butter = butter - cc_butter - pb_butter

    # Calculate the amount of butter used for sugar cookies
    sugar_butter = remaining_butter * 1/3

    # Calculate the amount of butter left
    butter_left = remaining_butter - sugar_butter

    result = butter_left
    return result

print(solution())