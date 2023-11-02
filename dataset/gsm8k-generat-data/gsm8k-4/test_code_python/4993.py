def solution():
    """Joe's pizzeria has an amazing promotion. If you buy any regular large pizza you can get the next 3 medium pizzas for $5 each. What are your total savings if the regular medium pizza price is $18 and you take full advantage of the promotion?"""
    # Define the regular price of a medium pizza
    REGULAR_MEDIUM_PRICE = 18

    # Calculate the price of 3 medium pizzas at the promotional rate
    PROMOTIONAL_MEDIUM_PRICE = 5 * 3

    # Calculate the total cost of the promotion (1 regular large pizza + 3 medium pizzas at promotional rate)
    PROMOTIONAL_COST = REGULAR_MEDIUM_PRICE + PROMOTIONAL_MEDIUM_PRICE

    # Calculate the total cost without the promotion (4 regular medium pizzas)
    REGULAR_COST = REGULAR_MEDIUM_PRICE * 4

    # Calculate the savings from taking advantage of the promotion
    SAVINGS = REGULAR_COST - PROMOTIONAL_COST

    result = SAVINGS
    return result

print(solution())