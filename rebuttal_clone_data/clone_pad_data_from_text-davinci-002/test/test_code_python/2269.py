def solution ():
    spools_purchased = 3
    feet_per_spool = 20
    feet_needed_per_necklace = 4
    total_feet = spools_purchased * feet_per_spool
    total_necklaces = total_feet // feet_needed_per_necklace
    result =  total_necklaces
    
    return result

print(solution())