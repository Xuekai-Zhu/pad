def solution():
    
    coke_parts = 2
    sprite_parts = 1
    mountaindew_parts = 3
    coke_ounces = 6
    sprite_ounces = (coke_ounces / coke_parts) * sprite_parts
    mountaindew_ounces = (coke_ounces / coke_parts) * mountaindew_parts
    total_ounces = coke_ounces + sprite_ounces + mountaindew_ounces
    result = total_ounces
    return result

print(solution())