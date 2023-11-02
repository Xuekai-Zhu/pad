def solution():
    """Daniel collects Russian dolls that normally cost $4 each. He saves enough money to buy 15 Russian dolls. However, the price suddenly drops to $3 each. How many Russian dolls can he buy now at the discounted price, given his savings?"""
    original_price = 4
    new_price = 3
    num_dolls_saved_for = 15
    money_saved = original_price * num_dolls_saved_for
    num_dolls_discounted = money_saved // new_price
    result = num_dolls_discounted
    return result

print(solution())