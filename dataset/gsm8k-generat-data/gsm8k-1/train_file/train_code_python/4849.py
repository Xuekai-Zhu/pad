def solution():
    """While bird watching, Gabrielle saw 5 robins, 4 cardinals, and 3 blue jays. Chase saw 2 robins, 3 blue jays, and 5 cardinals. How many more birds, in percentage, did Gabrielle saw than Chase?"""
    gabrielle_robins = 5
    gabrielle_cardinals = 4
    gabrielle_blue_jays = 3
    
    chase_robins = 2
    chase_cardinals = 5
    chase_blue_jays = 3
    
    gabrielle_total_birds = gabrielle_robins + gabrielle_cardinals + gabrielle_blue_jays
    chase_total_birds = chase_robins + chase_cardinals + chase_blue_jays
    
    difference = gabrielle_total_birds - chase_total_birds
    percentage_difference = (difference / chase_total_birds) * 100
    
    result = percentage_difference
    
    return result

print(solution())