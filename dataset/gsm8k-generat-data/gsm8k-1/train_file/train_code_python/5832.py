def solution():
    """In a shop, there is a sale of clothes. Every shirt costs $5, every hat $4, and a pair of jeans $10. How much do you need to pay for three shirts, two pairs of jeans, and four hats?"""
    shirts = 3
    jeans = 2
    hats = 4

    cost_of_shirts = shirts * 5
    cost_of_jeans = jeans * 10
    cost_of_hats = hats * 4

    total_cost = cost_of_shirts + cost_of_jeans + cost_of_hats
    result = total_cost
    return result

print(solution())