def solution():
    
    uniforms = 12
    coats = uniforms * 6
    techs = uniforms / 2
    total_items = uniforms + coats
    items_per_tech = total_items / techs
    result = items_per_tech
    return result

print(solution())