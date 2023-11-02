def solution():
    """Barry goes to a shop to buy a shirt he'd been admiring for quite some time. He tells the attendant that it's his birthday so she decides to give him a 15% special discount. The price tag on the shirt says $80. How much is he supposed to pay now, considering the special discount?"""
    original_price = 80
    discount = 0.15
    discounted_price = original_price - (discount * original_price)
    result = discounted_price
    return result

print(solution())