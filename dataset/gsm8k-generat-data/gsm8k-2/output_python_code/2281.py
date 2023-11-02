def solution():
    """Marcus wants to buy a new pair of shoes. He decided to pay not more than $130 for them. He found a pair for $120, on which he got a discount of 30%. How much money will he manage to save by buying these shoes and not spending the assumed maximum amount?"""
    max_price = 130
    discount_price = 120 * 0.7
    savings = max_price - discount_price
    result = savings
    return result

print(solution())