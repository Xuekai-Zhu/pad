def solution():
    
    total_frogs = 27
    mutated_frogs = 5 + 2 + 2
    mutation_percentage = (mutated_frogs / total_frogs) * 100
    result = round(mutation_percentage)
    return result

print(solution())