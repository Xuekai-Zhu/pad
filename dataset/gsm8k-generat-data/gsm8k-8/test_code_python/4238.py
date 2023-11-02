def solution():
    # Define the regular price of the sandwich
    sandwich_price = 8

    # Apply the coupon discount
    discounted_price = sandwich_price - (0.25 * sandwich_price)

    # Add the avocado upgrade
    upgraded_price = discounted_price + 1

    # Calculate the total cost of the meal
    total_cost = upgraded_price + 3 + 12

    # Calculate the cost of the drink
    drink_cost = total_cost - upgraded_price - 3

    result = drink_cost
    return result

print(solution())