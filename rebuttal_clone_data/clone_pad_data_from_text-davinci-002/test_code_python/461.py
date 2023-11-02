def solution():
    manuscripts = 10
    pages_per_manuscript = 400
    cost_per_page = 0.05
    cost_per_manuscript = 5.00
    total_cost = (manuscripts * pages_per_manuscript * cost_per_page) + (manuscripts * cost_per_manuscript)
    result = total_cost
    
    return result

print(solution())