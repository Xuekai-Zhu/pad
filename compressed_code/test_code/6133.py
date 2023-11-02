def solution():
    
    pages = 400
    copies = 10
    cost_per_page = 0.05
    cost_per_manuscript = 5.00
    total_pages = pages * copies
    copying_cost = total_pages * cost_per_page
    binding_cost = copies * cost_per_manuscript
    total_cost = copying_cost + binding_cost
    result = total_cost
    return result

print(solution())