def solution():
    """A one-year subscription to a newspaper is offered with a 45% discount. How much does the discounted subscription cost if a subscription normally costs $80?"""
    normal_price = 80
    discount_percent = 45
    discount_amount = normal_price * (discount_percent / 100)
    discounted_price = normal_price - discount_amount
    result = discounted_price
    return result

print(solution())