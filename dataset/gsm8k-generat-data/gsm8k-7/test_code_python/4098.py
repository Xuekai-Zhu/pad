def solution():
    thermos_size = 20  # ounces
    milk_per_cup = 0.5  # cup
    coffee_per_cup = thermos_size / 2 - milk_per_cup
    cups_per_day = 2
    days_per_week = 5

    # Calculate the total amount of coffee consumed in one week
    total_coffee_all = coffee_per_cup * cups_per_day * days_per_week

    # Calculate the new amount of coffee to be consumed after drinking 1/4 of the original amount
    total_coffee_new = total_coffee_all * 0.25

    result = total_coffee_new
    return result

print(solution())