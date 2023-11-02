def solution():
    gabrielle_robins = 5
    gabrielle_cardinals = 4
    gabrielle_blue_jays = 3
    gabrielle_total = gabrielle_robins + gabrielle_cardinals + gabrielle_blue_jays
    
    chase_robins = 2
    chase_cardinals = 5
    chase_blue_jays = 3
    chase_total = chase_robins + chase_cardinals + chase_blue_jays
    
    difference = gabrielle_total - chase_total
    gabrielle_percentage = (gabrielle_total / chase_total) * 100
    result = gabrielle_percentage - 100
    
    return result

print(solution())