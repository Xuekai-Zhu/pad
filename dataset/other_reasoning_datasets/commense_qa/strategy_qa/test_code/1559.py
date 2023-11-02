def solution():
    has_armor = False
    has_range_weapons = False
    if not has_armor and not has_range_weapons:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())