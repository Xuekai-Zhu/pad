def solution():
    """Trevor and two of his neighborhood friends go to the toy shop every year to buy toys. Trevor always spends $20 more than his friend Reed on toys, 
    and Reed spends 2 times as much money as their friend Quinn on the toys. 
    If Trevor spends $80 every year to buy his toys, calculate how much money in total the three spend in 4 years."""
    trevor_spends = 80
    reed_spends = trevor_spends - 20
    quinn_spends = reed_spends / 2
    total_spends_per_year = trevor_spends + reed_spends + quinn_spends
    total_spends_in_four_years = total_spends_per_year * 4
    result = total_spends_in_four_years
    
    return result

print(solution())