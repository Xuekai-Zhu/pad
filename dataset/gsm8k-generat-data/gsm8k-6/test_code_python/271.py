def solution():
    # Calculate the number of lilies to buy
    lilies = (3/4) * 20  
    
    # Calculate the total cost of roses and lilies
    total_cost = (20 * 5) + (lilies * 2 * 5)  # each lily costs twice as much as each rose
    
    result = total_cost
    return result

print(solution())