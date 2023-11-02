def solution():
    """Hannah bought a new washing machine for $100 and a dryer that costs $30 less. Hannah got a 10% discount for buying two appliances. How much did Hannah pay for the two appliances after the discount?"""
    washing_machine_price = 100
    dryer_price = washing_machine_price - 30
    total_price = washing_machine_price + dryer_price
    discount = total_price * 0.1
    discounted_price = total_price - discount
    result = discounted_price
    return result

print(solution())