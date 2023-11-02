def solution():
    """Daniela goes shopping during a sale. She finds out that the store has 40 percent off on shoes and 20 percent off dresses. If Daniela buys 2 pairs of shoes originally priced at $50 a pair and a dress originally priced at $100, how much money does she spend?"""
    shoe_price = 50
    dress_price = 100
    shoe_discount = 0.4
    dress_discount = 0.2
    total_shoe_price = 2 * shoe_price * (1 - shoe_discount)
    total_dress_price = dress_price * (1 - dress_discount)
    total_price = total_shoe_price + total_dress_price
    result = total_price
    return result

print(solution())