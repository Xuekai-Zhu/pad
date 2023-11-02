def solution():
    
    shampoo_cost = 10
    conditioner_cost = 10
    lotion_cost = 6
    num_lotions = 3
    total_cost = (shampoo_cost * 2) + (lotion_cost * num_lotions)
    amount_needed_for_shipping = 50 - total_cost
    result = amount_needed_for_shipping
    return result

print(solution())