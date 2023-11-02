def solution():
    """Barry goes to a shop to buy a shirt he'd been admiring for quite some time. He tells the attendant that it's his birthday so she decides to give him a 15% special discount. The price tag on the shirt says $80. How much is he supposed to pay now, considering the special discount?"""
    original_price = 80
    discount_percent = 15
    discount_amount = original_price * (discount_percent / 100)
    sale_price = original_price - discount_amount
    result = sale_price
    return result

print(solution())