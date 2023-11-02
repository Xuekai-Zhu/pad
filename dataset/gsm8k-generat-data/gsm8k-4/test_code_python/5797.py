def solution():
    """At a coffee shop, 7 customers order coffee at $5 each and 8 customers order tea at $4 each. How much money did the coffee shop make?"""
    # Define the price of coffee and tea
    coffee_price = 5
    tea_price = 4

    # Calculate the total amount earned from coffee orders
    coffee_total = 7 * coffee_price

    # Calculate the total amount earned from tea orders
    tea_total = 8 * tea_price

    # Calculate the total amount earned
    total_earned = coffee_total + tea_total

    # return the result
    result = total_earned
    return result

print(solution())