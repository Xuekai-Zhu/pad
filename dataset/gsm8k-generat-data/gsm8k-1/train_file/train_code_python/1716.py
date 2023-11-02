def solution():
    """A store sold a certain brand of jeans for $40. They only have few pairs of jeans left so they decided to give 10% discount on every two pairs of jeans bought by a customer at any one time. How much will a customer pay for 3 pairs of jeans?"""
    jeans_price = 40
    num_jeans = 3
    num_discounted_pairs = num_jeans // 2
    total_price = jeans_price * num_jeans
    discount_amount = num_discounted_pairs * jeans_price * 0.1
    final_price = total_price - discount_amount
    result = final_price
    return result

print(solution())