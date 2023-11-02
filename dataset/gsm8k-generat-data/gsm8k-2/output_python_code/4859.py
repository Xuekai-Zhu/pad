def solution():
    """In a factory, there are 3 machines working 23 hours a day. The owner decided to buy a fourth machine, which works only 12 hours a day. One machine can produce 2 kg of material every hour. The factory sells the produced material for $50 per 1 kg. How much can this factory earn in one day?"""
    machines_time = 23 * 3 + 12
    machines_total = 4
    production_rate = 2 * machines_total
    production_total = production_rate * machines_time
    income = production_total * 50
    result = income
    return result

print(solution())