def solution():
    
    cost_hamburger = 3
    cost_fries = 1.2
    cost_soda = 0.5
    cost_spaghetti = 2.7
    
    total_cost = (5*cost_hamburger) + (4*cost_fries) + (5*cost_soda) + cost_spaghetti
    cost_per_person = total_cost / 5
    
    result = cost_per_person
    return result

print(solution())