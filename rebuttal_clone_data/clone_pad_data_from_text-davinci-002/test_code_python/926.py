def solution():
    guest_bathroom_sets = 2
    master_bathroom_sets = 4
    price_guest_bathroom = 40
    price_master_bathroom = 50
    percent_off = 20
    total_price_guest_bathroom = (guest_bathroom_sets * price_guest_bathroom)
    total_price_master_bathroom = (master_bathroom_sets * price_master_bathroom)
    total_price = total_price_guest_bathroom + total_price_master_bathroom
    discounted_total = total_price - (total_price * (percent_off/100))
    result = discounted_total
    
    return result

print(solution())