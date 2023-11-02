def solution():
    
    names = ['Jessica', 'Tori', 'Lily', 'Patrice']
    total_bracelets = sum([len(name) for name in names])
    total_cost = total_bracelets * 2
    result = total_cost
    return result

print(solution())