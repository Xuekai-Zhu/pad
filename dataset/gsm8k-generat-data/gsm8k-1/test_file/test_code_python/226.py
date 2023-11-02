def solution():
    """Mark buys a fleet of 12 cars for his company. Each car sells for $20,000. He pays 10% tax on the cars and then another $1000 for registration on each of them. How much does he pay for everything?"""
    num_cars = 12
    price_per_car = 20000
    tax_rate = 0.1
    registration_fee = 1000
    total_cost = num_cars * (price_per_car + price_per_car * tax_rate + registration_fee)
    result = total_cost
    return result

print(solution())