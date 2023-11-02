def solution():
    """Alvin owns coconut trees that yield 5 coconuts each. If a coconut can be sold for $3 and Alvin needs $90, how many coconut trees does he have to harvest?"""
    coconuts_per_tree = 5
    price_per_coconut = 3
    total_profit_needed = 90
    coconuts_needed = total_profit_needed / price_per_coconut
    trees_needed = coconuts_needed / coconuts_per_tree
    result = trees_needed
    return result

print(solution())