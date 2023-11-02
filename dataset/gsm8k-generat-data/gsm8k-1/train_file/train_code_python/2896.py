def solution():
    """Juanita goes through 1 bottle of sunscreen a month. She likes to stock up for the entire year when a certain website offers 30% off her entire purchase. If each bottle is $30.00 how much will all of the sunscreen cost after the discount?"""
    bottles_per_year = 12
    cost_per_bottle = 30
    discount_percent = 30
    cost_before_discount = bottles_per_year * cost_per_bottle
    discount_amount = cost_before_discount * (discount_percent / 100)
    cost_after_discount = cost_before_discount - discount_amount
    result = cost_after_discount
    return result

print(solution())