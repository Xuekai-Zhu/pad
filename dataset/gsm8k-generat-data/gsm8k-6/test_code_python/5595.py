def solution():
    # Calculate the number of times the cost is halved in 30 years
    num_halving = 30 // 10
    
    # Calculate the final cost of the ticket
    final_cost = 1000000 / (2 ** num_halving)  # the cost is halved num_halving times
    
    result = final_cost
    return result

print(solution())