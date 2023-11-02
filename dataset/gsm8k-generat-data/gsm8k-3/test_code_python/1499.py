def solution():
    """A taco truck is selling soft tacos for $2 and hard shell tacos for $5 during the lunch rush. The first group of customers is a family that buys four hard shell tacos and three soft tacos. The rest of the customers in the lunch rush only buy two soft tacos each. There were ten customers after the family. How many dollars did the taco truck make during the lunch rush?"""
    # Define the prices of soft and hard shell tacos
    SOFT_TACO_PRICE = 2
    HARD_TACO_PRICE = 5

    # Calculate the earnings from the family's order
    family_earnings = (4 * HARD_TACO_PRICE) + (3 * SOFT_TACO_PRICE)

    # Calculate the earnings from the rest of the customers
    rest_customers_earnings = 10 * (2 * SOFT_TACO_PRICE)

    # Calculate the total earnings during the lunch rush
    total_earnings = family_earnings + rest_customers_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())