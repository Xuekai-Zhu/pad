def solution():
    
    guest_sets = 2
    master_sets = 4
    guest_set_price = 40
    master_set_price = 50
    discount = 0.2
    total_cost = (guest_sets * guest_set_price + master_sets * master_set_price) * (1 - discount)
    result = total_cost
    return result

print(solution())