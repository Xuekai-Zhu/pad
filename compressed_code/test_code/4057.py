def solution():
    
    total_parents = 120
    excellent_percent = 0.15
    very_satisfactory_percent = 0.6
    satisfactory_percent = 0.8
    excellent_count = total_parents * excellent_percent
    very_satisfactory_count = total_parents * very_satisfactory_percent
    remaining_parents_count = total_parents - excellent_count - very_satisfactory_count
    satisfactory_count = remaining_parents_count * satisfactory_percent
    needs_improvement_count = total_parents - excellent_count - very_satisfactory_count - satisfactory_count
    result = needs_improvement_count
    return result

print(solution())