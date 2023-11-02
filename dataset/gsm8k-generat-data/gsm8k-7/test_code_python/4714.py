def solution():
    total_frogs = 5 + 2 + 2 + 18
    mutated_frogs = 5 + 2 + 2
    
    # Calculate the percentage of frogs that have mutated
    percentage_mutated = (mutated_frogs / total_frogs) * 100
    
    # Round the percentage to the nearest integer
    rounded_percentage = round(percentage_mutated)
    
    result = rounded_percentage
    return result

print(solution())