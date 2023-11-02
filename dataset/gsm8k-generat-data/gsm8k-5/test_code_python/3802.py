def solution():
    latte_cost = 3.75  # Cost of a latte
    croissant_cost = 3.50  # Cost of a croissant
    cookie_cost = 1.25  # Cost of a cookie
    days_per_week = 7  # Number of days in a week

    # Calculate the total cost of coffee and pastry for a week
    total_cost = (latte_cost + croissant_cost) * days_per_week + (5 * cookie_cost)

    # Calculate the amount left on the gift card after a week
    amount_left = 100 - total_cost
    result = amount_left
    return result

print(solution())