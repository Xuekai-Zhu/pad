def solution():
    burger_meal_price = 6.00  # Clinton buys a burger meal for $6.00
    upsize_price = 1.00  # Clinton pays an extra $1.00 to upsize his fries and drinks
    days = 5  # Clinton buys this meal every day for 5 days

    # Calculate the total amount Clinton spends on lunch
    total_spent = (burger_meal_price + upsize_price) * days
    result = total_spent
    return result

print(solution())