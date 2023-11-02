def solution():
    # Calculate the total amount of food needed for three months
    food_per_day = 1  # 1 cup of food per day (1/2 cup in the morning and 1/2 cup in the afternoon)
    days_per_month = 31 + 31 + 28  # number of days in December, January and February
    total_food = food_per_day * 2 * days_per_month  # amount of food per day * 2 (morning and afternoon) * number of days
    result = total_food / 2  # convert from cups to half-cups
    return result

print(solution())