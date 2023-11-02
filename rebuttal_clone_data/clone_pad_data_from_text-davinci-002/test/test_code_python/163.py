def solution():
    cost_per_page = 0.1
    total_pages = 25
    total_copies = 7
    cost_to_print = total_pages * total_copies * cost_per_page
    cost_of_pens = 7 * 1.5
    total_cost = cost_to_print + cost_of_pens
    cash_paid = 40
    change_due = cash_paid - total_cost
    result = change_due
    
    return result

print(solution())