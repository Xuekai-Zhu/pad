def solution():
    butter = 10  # Liza bought 10 kilograms of butter
    chocolate_chip = butter / 2  # Liza used one-half of the butter for chocolate chip cookies
    peanut_butter = butter / 5  # Liza used one-fifth of the butter for peanut butter cookies
    remaining_butter = butter - chocolate_chip - peanut_butter  # Liza has this much butter left
    sugar_cookies = remaining_butter / 3  # Liza used one-third of the remaining butter for sugar cookies
    butter_left = remaining_butter - sugar_cookies  # Liza has this much butter left after making all three kinds of cookies
    result = butter_left
    return result

print(solution())