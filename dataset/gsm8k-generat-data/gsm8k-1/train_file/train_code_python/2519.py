def solution():
    """Rockefeller Army Base has 3000 more than twice as many guns as Grenada Army Base, 400 less than thrice as many war tractors as Grenada Army Base, and 30 times as many soldier uniforms as Grenada Army Base reserved for its national protection. How many total war supplies does Rockefeller have if Grenada's war supplies are equally divided among the 6000 war supplies they have in total?"""
    grenada_supplies = 6000
    grenada_guns = grenada_supplies // 3
    grenada_tractors = grenada_supplies
    grenada_uniforms = grenada_supplies * 30
    
    rockefeller_guns = grenada_guns * 2 + 3000
    rockefeller_tractors = grenada_tractors * 3 - 400
    rockefeller_uniforms = grenada_uniforms * 2
    
    total_supplies = rockefeller_guns + rockefeller_tractors + rockefeller_uniforms
    
    result = total_supplies
    return result

print(solution())