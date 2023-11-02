def solution():
    """In a shop, there is a sale of clothes. Every shirt costs $5, every hat $4, and a pair of jeans $10. How much do you need to pay for three shirts, two pairs of jeans, and four hats?"""
    shirt_price = 5
    jeans_price = 10
    hat_price = 4
    total_cost = (3 * shirt_price) + (2 * jeans_price) + (4 * hat_price)
    result = total_cost
    return result

print(solution())