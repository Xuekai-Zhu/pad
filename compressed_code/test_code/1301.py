def solution():
    
    shampoo_cost = 10
    conditioner_cost = 10
    lotion_cost = 6
    total_cost = (shampoo_cost * 2) + (lotion_cost * 3)
    needed_cost_for_free_shipping = 50
    difference = needed_cost_for_free_shipping - total_cost
    result = difference
    return result

print(solution())