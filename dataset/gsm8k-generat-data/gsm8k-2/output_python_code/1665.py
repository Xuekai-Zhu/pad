def solution():
    """Calvin buys a pack of chips, for $0.50, from the vending machine at lunch, 5 days a week. After 4 weeks, how much money has Calvin spent on chips?"""
    pack_price = 0.5
    packs_per_week = 5
    weeks = 4
    total_packs = packs_per_week * weeks
    total_spent = total_packs * pack_price
    result = total_spent
    return result

print(solution())