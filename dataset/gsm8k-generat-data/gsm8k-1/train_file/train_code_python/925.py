def solution():
    """Bailey needs to buy 2 new sets of towels for the guest bathroom and 4 new sets for her master bathroom. The set of towels for the guest bathroom are $40.00 each and the master bathroom set is $50.00 each. The store is currently offering 20% off so how much will Bailey spend on towel sets?"""
    guest_sets = 2
    master_sets = 4
    guest_set_price = 40
    master_set_price = 50
    discount = 0.2
    total_cost = (guest_sets * guest_set_price + master_sets * master_set_price) * (1 - discount)
    result = total_cost
    return result

print(solution())