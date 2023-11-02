def solution():
    
    total_computers = 20
    unfixable_computers = 0.2 * total_computers
    waiting_computers = 0.4 * total_computers
    fixed_computers = total_computers - unfixable_computers - waiting_computers
    result = fixed_computers
    return result

print(solution())