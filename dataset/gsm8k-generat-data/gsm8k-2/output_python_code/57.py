def solution():
    """Liza bought 10 kilograms of butter to make cookies. She used one-half of it for chocolate chip cookies, one-fifth of it for peanut butter cookies, and one-third of the remaining butter for sugar cookies. How many kilograms of butter are left after making those three kinds of cookies?"""
    butter = 10
    chocolate_chip_butter = butter / 2
    peanut_butter_butter = butter / 5
    remaining_butter = butter - chocolate_chip_butter - peanut_butter_butter
    sugar_butter = remaining_butter / 3
    total_butter_used = chocolate_chip_butter + peanut_butter_butter + sugar_butter
    butter_left = butter - total_butter_used
    result = butter_left
    return result

print(solution())