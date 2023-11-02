def solution():
    """A one-year subscription to a newspaper is offered with a 45% discount. How much does the discounted subscription cost if a subscription normally costs $80?"""
    subscription_cost = 80
    discount_percent = 45
    discount_amount = subscription_cost * (discount_percent/100)
    discounted_subscription_cost = subscription_cost - discount_amount
    result = discounted_subscription_cost
    return result

print(solution())