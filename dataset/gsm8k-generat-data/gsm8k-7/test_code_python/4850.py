def solution():
    gabrielle_robins = 5
    gabrielle_cardinals = 4
    gabrielle_blue_jays = 3
    
    chase_robins = 2
    chase_blue_jays = 3
    chase_cardinals = 5
    
    # Calculate the total number of birds that Gabrielle saw
    gabrielle_total_birds = gabrielle_robins + gabrielle_cardinals + gabrielle_blue_jays
    
    # Calculate the total number of birds that Chase saw
    chase_total_birds = chase_robins + chase_blue_jays + chase_cardinals
    
    # Calculate how many more birds Gabrielle saw than Chase
    difference = gabrielle_total_birds - chase_total_birds
    
    # Calculate the percentage difference
    percentage = (difference / chase_total_birds) * 100
    
    result = percentage
    return result

print(solution())