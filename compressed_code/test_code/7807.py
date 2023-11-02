def solution():
    
    iron_available = 400
    iron_per_horseshoe = 2
    total_horseshoes_possible = iron_available / iron_per_horseshoe

    farms_horses = 2 * 2
    stables_horses = 2 * 5
    total_horses_to_shoe = farms_horses + stables_horses

    horseshoes_used = total_horses_to_shoe * 4  
    horseshoes_left = total_horseshoes_possible - horseshoes_used

    riding_school_horses = horseshoes_left / 4  
    result = riding_school_horses
    return result

print(solution())