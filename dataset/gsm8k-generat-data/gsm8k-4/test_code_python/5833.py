def solution():
    """In a shop, there is a sale of clothes. Every shirt costs $5, every hat $4, and a pair of jeans $10. How much do you need to pay for three shirts, two pairs of jeans, and four hats?"""
    # Define the prices of shirts, hats, and jeans
    shirt_price = 5
    hat_price = 4
    jeans_price = 10

    # Calculate the total cost of three shirts, two pairs of jeans, and four hats
    total_cost = (3 * shirt_price) + (2 * jeans_price) + (4 * hat_price)

    # Return the total cost
    result = total_cost
    return result

print(solution())