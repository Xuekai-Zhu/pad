def solution():
    """Five friends eat at a fast-food chain and order the following: 5 pieces of hamburger that cost $3 each; 4 sets of French fries that cost $1.20; 5 cups of soda that cost $0.5 each; and 1 platter of spaghetti that cost $2.7. How much will each of them pay if they will split the bill equally?"""
    cost_hamburger = 3
    cost_fries = 1.2
    cost_soda = 0.5
    cost_spaghetti = 2.7
    
    total_cost = (5*cost_hamburger) + (4*cost_fries) + (5*cost_soda) + cost_spaghetti
    cost_per_person = total_cost / 5
    
    result = cost_per_person
    return result

print(solution())