def solution():
    
    coconut_yield = 5
    coconut_price = 3
    target_amount = 90
    coconuts_needed = target_amount / coconut_price
    trees_needed = coconuts_needed / coconut_yield
    result = trees_needed
    return result

print(solution())