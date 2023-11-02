def solution():
    
    uniforms = 12
    coats = 6 * uniforms
    lab_techs = uniforms / 2
    total_items = uniforms + coats
    items_per_tech = total_items / lab_techs
    result = items_per_tech
    return result

print(solution())