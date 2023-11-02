def solution():
    total_butter = 10  # kilograms of butter bought
    chocolate_chip_butter = (1/2) * total_butter  # kilograms of butter used for chocolate chip cookies
    peanut_butter_butter = (1/5) * total_butter  # kilograms of butter used for peanut butter cookies
    remaining_butter = total_butter - chocolate_chip_butter - peanut_butter_butter  # kilograms of remaining butter
    sugar_cookie_butter = (1/3) * remaining_butter  # kilograms of butter used for sugar cookies
    remaining_butter -= sugar_cookie_butter  # subtracting the butter used for sugar cookies from remaining butter
    result = remaining_butter
    return result

print(solution())