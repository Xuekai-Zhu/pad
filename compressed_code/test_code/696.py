def solution():
    
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