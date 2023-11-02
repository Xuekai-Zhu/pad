def solution():
    """In a factory, there are 3 machines working 23 hours a day. The owner decided to buy a fourth machine, which works only 12 hours a day. One machine can produce 2 kg of material every hour. The factory sells the produced material for $50 per 1 kg. How much can this factory earn in one day?"""
    num_machines = 4
    hours_per_day = 23 + 12
    production_rate = 2 * num_machines
    total_production = production_rate * hours_per_day
    price_per_kg = 50
    total_earnings = total_production * price_per_kg
    result = total_earnings

    return result

print(solution())