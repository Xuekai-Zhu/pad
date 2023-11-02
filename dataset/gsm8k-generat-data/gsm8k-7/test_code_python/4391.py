def solution():
    num_quarters = 160
    cost_of_dress = 35
    
    # Calculate the number of quarters needed to pay for the dress
    num_quarters_needed = cost_of_dress / 0.25
    
    # Calculate the number of quarters left after paying for the dress
    num_quarters_left = num_quarters - num_quarters_needed
    
    result = num_quarters_left
    return result

print(solution())