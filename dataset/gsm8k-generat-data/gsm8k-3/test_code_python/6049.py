def solution():
    """If the price of a bag of cherries is $5 when the price of a bag of olives is $7, how much would Jordyn pay for buying 50 bags of each fruit and a 10% discount?"""
    # Define the prices per bag
    CHERRY_PRICE = 5
    OLIVE_PRICE = 7

    # Define the number of bags purchased
    bags = 50

    # Calculate the total cost before discount
    cherry_cost = CHERRY_PRICE * bags
    olive_cost = OLIVE_PRICE * bags
    total_cost = cherry_cost + olive_cost

    # Apply the discount
    total_cost *= 0.9

    # Display the total cost
    result = total_cost
    return result

print(solution())