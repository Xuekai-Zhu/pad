def solution():
    
    coke_parts = 2
    sprite_parts = 1
    mdew_parts = 3
    total_parts = coke_parts + sprite_parts + mdew_parts
    coke_ounces = 6
    sprite_ounces = coke_ounces * (sprite_parts / coke_parts)
    mdew_ounces = coke_ounces * (mdew_parts / coke_parts)
    total_ounces = coke_ounces + sprite_ounces + mdew_ounces
    result = total_ounces
    return result

print(solution())