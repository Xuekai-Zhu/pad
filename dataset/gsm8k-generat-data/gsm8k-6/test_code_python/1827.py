def solution():
    # Calculate the number of eggs Lisa makes for her family each day
    eggs_per_day = 2*(4) + 3 + 2  # 2 eggs for each of her 4 children, 3 eggs for her husband, and 2 for herself

    # Multiply by the number of days in a year (assuming a 365-day year)
    eggs_per_year = eggs_per_day * 365

    result = eggs_per_year
    return result

print(solution())