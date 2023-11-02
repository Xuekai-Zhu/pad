def solution():
    """The Franzia wine is three times as old as the Carlo Rosi, while the Carlo Rosi is four times older than the Twin Valley. Calculate the total age of the three brands of wine if the Carlo Rosi is 40 years old."""
    
    carlo_rosi_age = 40
    twin_valley_age = carlo_rosi_age / 4
    franzia_age = carlo_rosi_age * 3
    
    total_age = carlo_rosi_age + twin_valley_age + franzia_age
    
    result = total_age
    
    return result

print(solution())