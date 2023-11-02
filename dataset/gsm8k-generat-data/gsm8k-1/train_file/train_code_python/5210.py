def solution():
    """Jake makes a drink that is 2 parts Coke, 1 part Sprite and 3 parts Mountain Dew. If the drink contains 6 ounces of Coke, how many ounces is the drink?"""
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