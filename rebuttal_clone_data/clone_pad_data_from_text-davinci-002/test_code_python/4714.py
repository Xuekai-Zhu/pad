def solution():
    total_frogs = 5 + 2 + 2 + 18
    mutated_frogs = 5 + 2 + 2
    mutated_percentage = mutated_frogs / total_frogs * 100
    result = round(mutated_percentage)
    return result

print(solution())