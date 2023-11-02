def solution():
    """Daniela goes shopping during a sale. She finds out that the store has 40 percent off on shoes and 20 percent off dresses.
    If Daniela buys 2 pairs of shoes originally priced at $50 a pair and a dress originally priced at $100, how much money does she spend?"""
    shoes_discount = 40
    dress_discount = 20
    shoes_price = 50
    dress_price = 100
    discounted_shoes_price = shoes_price * (100 - shoes_discount) / 100
    discounted_dress_price = dress_price * (100 - dress_discount) / 100
    total_price = (discounted_shoes_price * 2) + discounted_dress_price
    result = total_price
    return result

print(solution())