def solution():
    """Juanita goes through 1 bottle of sunscreen a month. She likes to stock up for the entire year when a certain website offers 30% off her entire purchase. If each bottle is $30.00 how much will all of the sunscreen cost after the discount?"""
    bottles_per_year = 12
    bottle_price = 30
    discount_percent = 30
    discount_amount = discount_percent / 100 * (bottles_per_year * bottle_price)
    total_price = (bottles_per_year * bottle_price) - discount_amount
    result = total_price
    return result

print(solution())