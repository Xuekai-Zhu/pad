def solution():
    """"In a shop, there is a sale of clothes. Every shirt costs $5, every hat $4, and a pair of jeans $10. How much do you need to pay for three shirts, two pairs of jeans, and four hats?"""
    # Define the prices of each item
    SHIRT_PRICE = 5
    HAT_PRICE = 4
    JEANS_PRICE = 10

    # Define the quantities of each item purchased
    shirts = 3
    hats = 4
    jeans = 2

    # Calculate the total cost of the shirts
    shirt_cost = shirts * SHIRT_PRICE

    # Calculate the total cost of the hats
    hat_cost = hats * HAT_PRICE

    # Calculate the total cost of the jeans
    jeans_cost = jeans * JEANS_PRICE

    # Calculate the total cost of all the items
    total_cost = shirt_cost + hat_cost + jeans_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())