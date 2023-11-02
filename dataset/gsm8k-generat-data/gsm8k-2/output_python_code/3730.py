def solution():
    """There are 6 times as many lab coats as uniforms in the lab. The number of lab techs is half of the number of uniforms. If there are 12 uniforms in the lab, and the lab techs share the coats and uniforms equally among them, how many coats and uniforms in total does each lab tech get?"""
    uniforms = 12
    coats = 6 * uniforms
    lab_techs = uniforms / 2
    total_items = uniforms + coats
    items_per_tech = total_items / lab_techs
    result = items_per_tech
    return result

print(solution())