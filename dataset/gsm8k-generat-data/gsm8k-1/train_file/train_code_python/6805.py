def solution():
    """Daniel collects Russian dolls that normally cost $4 each. He saves enough money to buy 15 Russian dolls. However, the price suddenly drops to $3 each. How many Russian dolls can he buy now at the discounted price, given his savings?"""
    original_price = 4
    discounted_price = 3
    num_dolls = 15
    original_cost = original_price * num_dolls
    discounted_cost = discounted_price * num_dolls
    num_dolls_discounted = discounted_cost / discounted_price
    result = num_dolls_discounted
    return result

print(solution())