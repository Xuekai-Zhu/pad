def solution():
    """James was doing some shopping in his favorite shop and he saw an offer on shoes that give him a second pair of shoes for half off the original price. He took the offer and took the first pair of shoes for $40 and the second one for $60. At the cashier, the lady told him that the offer applies strictly to the cheaper pair of shoes, and also that he was selected for an extra discount of a fourth off the total amount. How much money did James end up paying for both pairs of shoes?"""
    first_pair_price = 40
    second_pair_price = 60
    cheaper_pair_price = min(first_pair_price, second_pair_price)
    discounted_pair_price = cheaper_pair_price / 2
    total_price = first_pair_price + second_pair_price - cheaper_pair_price + discounted_pair_price
    total_price = total_price - (total_price * 0.25)
    result = total_price
    return result

print(solution())