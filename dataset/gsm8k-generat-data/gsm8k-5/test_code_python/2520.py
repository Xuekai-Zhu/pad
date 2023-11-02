def solution():
    grenada_supplies = 6000  # Grenada has 6000 war supplies in total
    grenada_guns = grenada_supplies / 3  # Grenada has one-third of the total supplies in guns
    grenada_tractors = (grenada_supplies + 400) / 3  # Grenada has one-third of the total supplies in war tractors, 400 more than Rockefeller
    grenada_uniforms = grenada_supplies / 30  # Grenada has one-thirtieth of the total supplies in soldier uniforms

    rockefeller_guns = 2 * grenada_guns + 3000  # Rockefeller has 3000 more than twice as many guns as Grenada
    rockefeller_tractors = 3 * grenada_tractors - 400  # Rockefeller has 400 less than thrice as many war tractors as Grenada
    rockefeller_uniforms = 30 * grenada_uniforms  # Rockefeller has 30 times as many soldier uniforms as Grenada

    total_supplies = grenada_supplies + rockefeller_guns + rockefeller_tractors + rockefeller_uniforms
    result = total_supplies
    return result

print(solution())