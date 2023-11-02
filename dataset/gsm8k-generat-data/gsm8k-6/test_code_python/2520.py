def solution():
    # Calculate the number of war supplies in Grenada
    grenada_supplies = 6000
    grenada_guns = grenada_supplies / 3  # one-third of the supplies are guns
    grenada_tractors = (grenada_supplies / 3) * 2  # two-thirds of the supplies are war tractors
    grenada_uniforms = grenada_supplies * 30  # thirty times the number of supplies are uniforms

    # Calculate the number of war supplies in Rockefeller
    rockefeller_guns = grenada_guns * 2 + 3000  # twice as many guns as Grenada, plus 3000 more
    rockefeller_tractors = grenada_tractors * 3 - 400  # thrice as many war tractors as Grenada, minus 400
    rockefeller_uniforms = grenada_uniforms * 1  # same number of soldier uniforms as Grenada

    total_supplies = rockefeller_guns + rockefeller_tractors + rockefeller_uniforms
    result = total_supplies
    return result

print(solution())