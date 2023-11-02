def solution():
    """Hannah bought a new washing machine for $100 and a dryer that costs $30 less. Hannah got a 10% discount for buying two appliances. How much did Hannah pay for the two appliances after the discount?"""
    washing_machine_cost = 100
    dryer_cost = washing_machine_cost - 30
    total_cost = washing_machine_cost + dryer_cost
    discount_percent = 10
    discount_amount = total_cost * (discount_percent / 100)
    discounted_total = total_cost - discount_amount
    result = discounted_total
    return result

print(solution())