def solution():
    """Rockefeller Army Base has 3000 more than twice as many guns as Grenada Army Base, 400 less than thrice as many war tractors as Grenada Army Base, and 30 times as many soldier uniforms as Grenada Army Base reserved for its national protection. How many total war supplies does Rockefeller have if Grenada's war supplies are equally divided among the 6000 war supplies they have in total?"""
    # Calculate the total number of war supplies Grenada has
    grenada_supplies = 6000

    # Calculate the number of war supplies each Grenada base has
    grenada_base_supplies = grenada_supplies / 2

    # Calculate the number of supplies at the Rockefeller Army Base
    guns = 2 * grenada_base_supplies + 3000
    war_tractors = 3 * grenada_base_supplies - 400
    soldier_uniforms = 30 * grenada_base_supplies
    total_supplies = guns + war_tractors + soldier_uniforms

    # Return the result
    result = total_supplies
    return result

print(solution())