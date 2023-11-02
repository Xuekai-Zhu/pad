def solution():
    """A one-year subscription to a newspaper is offered with a 45% discount. How much does the discounted subscription cost if a subscription normally costs $80?"""
    percent_discount = 45
    normal_cost = 80
    discount = normal_cost * (percent_discount / 100)
    discounted_cost = normal_cost - discount
    result = discounted_cost
    return result

print(solution())