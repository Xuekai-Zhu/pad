def solution():
    """Alvin owns coconut trees that yield 5 coconuts each. If a coconut can be sold for $3 and Alvin needs $90, how many coconut trees does he have to harvest?"""
    coconut_yield = 5
    coconut_price = 3
    target_amount = 90
    coconuts_needed = target_amount / coconut_price
    trees_needed = coconuts_needed / coconut_yield
    result = trees_needed
    return result

print(solution())