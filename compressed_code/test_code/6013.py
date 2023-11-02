def solution():
    
    cost_per_page = 0.10
    pages_per_copy = 25
    num_copies = 7
    num_pens = 7
    cost_of_printing = cost_per_page * pages_per_copy * num_copies
    cost_of_pens = num_pens * 1.50
    total_cost = cost_of_printing + cost_of_pens
    
    amount_paid = 2 * 20
    change = amount_paid - total_cost
    result = change
    
    return result

print(solution())