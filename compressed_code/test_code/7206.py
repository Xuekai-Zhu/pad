def solution():
    
    lychees_in_carton = 500
    sold_lychees = lychees_in_carton / 2
    remaining_lychees = lychees_in_carton - sold_lychees
    eaten_lychees = remaining_lychees * (3/5)
    lychees_remaining = remaining_lychees - eaten_lychees
    result = lychees_remaining
    return result

print(solution())