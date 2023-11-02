def solution():
    # Define the amount of butter Liza bought
    total_butter = 10

    # Calculate the amount of butter used for chocolate chip cookies
    choc_chip_butter = total_butter * 0.5

    # Calculate the amount of butter used for peanut butter cookies
    peanut_butter_butter = total_butter * 0.2

    # Calculate the remaining butter after making chocolate chip and peanut butter cookies
    remaining_butter1 = total_butter - choc_chip_butter - peanut_butter_butter

    # Calculate the amount of butter used for sugar cookies
    sugar_cookie_butter = remaining_butter1 * (1/3)

    # Calculate the remaining butter after making all three kinds of cookies
    remaining_butter2 = remaining_butter1 - sugar_cookie_butter

    result = remaining_butter2
    return result

print(solution())