def solution():
    
    budget = 15
    artichoke_price = 1.25
    max_artichokes = budget // artichoke_price
    ounces_per_artichoke = 5/3
    max_ounces = max_artichokes * ounces_per_artichoke
    result = max_ounces
    return result

print(solution())