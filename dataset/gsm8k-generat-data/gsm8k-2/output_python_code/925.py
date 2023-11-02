def solution():
    """Bailey needs to buy 2 new sets of towels for the guest bathroom and 4 new sets for her master bathroom. The set of towels for the guest bathroom are $40.00 each and the master bathroom set is $50.00 each. The store is currently offering 20% off so how much will Bailey spend on towel sets?"""
    guest_bathroom_sets = 2
    master_bathroom_sets = 4
    guest_bathroom_set_price = 40
    master_bathroom_set_price = 50
    discount_percentage = 20
    total_guest_bathroom_set_price = guest_bathroom_sets * guest_bathroom_set_price
    total_master_bathroom_set_price = master_bathroom_sets * master_bathroom_set_price
    total_price_before_discount = total_guest_bathroom_set_price + total_master_bathroom_set_price
    discount_amount = (discount_percentage / 100) * total_price_before_discount
    total_price_after_discount = total_price_before_discount - discount_amount
    result = total_price_after_discount
    return result

print(solution())