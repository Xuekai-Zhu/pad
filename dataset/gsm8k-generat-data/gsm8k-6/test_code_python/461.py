def solution():
    # Calculate the total cost of printing and binding 1 manuscript
    cost_per_manuscript = 0.05 * 400 + 5
    
    # Calculate the total cost of printing and binding 10 manuscripts
    total_cost = cost_per_manuscript * 10
    result = total_cost
    return result

print(solution())