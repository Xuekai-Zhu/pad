def solution():
    beef_pounds = 1000
    beef_price_per_pound = 8.0

    chicken_pounds = beef_pounds * 2
    chicken_price_per_pound = 3.0

    # Calculate the cost of the beef
    beef_cost = beef_pounds * beef_price_per_pound

    # Calculate the cost of the chicken
    chicken_cost = chicken_pounds * chicken_price_per_pound

    # Calculate the total cost of everything
    total_cost = beef_cost + chicken_cost
    result = total_cost
    return result

print(solution())