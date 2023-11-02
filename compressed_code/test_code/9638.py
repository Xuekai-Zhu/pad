def solution():
    
    friend_names = ['Jessica', 'Tori', 'Lily', 'Patrice']
    total_bracelets = 0
    for name in friend_names:
        name_length = len(name)
        total_bracelets += name_length
    cost_per_bracelet = 2
    total_cost = total_bracelets * cost_per_bracelet
    result = total_cost
    return result

print(solution())