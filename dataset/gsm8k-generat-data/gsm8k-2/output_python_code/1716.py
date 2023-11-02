def solution():
    """A store sold a certain brand of jeans for $40. They only have few pairs of jeans left so they decided to give 10% discount on every two pairs of jeans bought by a customer at any one time. How much will a customer pay for 3 pairs of jeans?"""
    jeans_price = 40
    pairs_of_jeans = 3 // 2
    total_price = pairs_of_jeans * jeans_price
    discount = pairs_of_jeans * (jeans_price * 0.1)
    if 3 % 2 == 1:
        total_price += jeans_price
    total_price -= discount
    result = total_price
    return result

print(solution())