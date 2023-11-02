def solution():
    """Joe's pizzeria has an amazing promotion. If you buy any regular large pizza you can get the next 3 medium pizzas for $5 each. What are your total savings if the regular medium pizza price is $18 and you take full advantage of the promotion?"""
    # Define the regular medium pizza price
    REGULAR_PRICE = 18

    # Calculate the total cost of 4 medium pizzas without the promotion
    regular_cost = REGULAR_PRICE * 4

    # Calculate the total cost of 1 large pizza and 3 medium pizzas with the promotion
    promo_cost = (REGULAR_PRICE + (3 * 5))

    # Calculate the total savings with the promotion
    total_savings = regular_cost - promo_cost

    # Display the total savings
    result = total_savings
    return result

print(solution())